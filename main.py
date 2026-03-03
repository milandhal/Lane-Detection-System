"""
Lane Lines Detection pipeline

Usage:
    main.py [--video] INPUT_PATH OUTPUT_PATH 

Options:

-h --help                               show this screen
--video                                 process video file instead of image
"""

import numpy as np
import matplotlib.image as mpimg
import cv2
from docopt import docopt
from CameraCalibration import CameraCalibration
from Thresholding import *
from PerspectiveTransformation import *
from LaneLines import *

try:
    from IPython.display import HTML, Video
except ImportError:
    pass

HAS_MOVIEPY = False
try:
    from moviepy.editor import VideoFileClip
    HAS_MOVIEPY = True
except Exception:
    pass

class FindLaneLines:
    """ This class is for parameter tunning.

    Attributes:
        ...
    """
    def __init__(self):
        """ Init Application"""
        self.calibration = CameraCalibration('camera_cal', 9, 6)
        self.thresholding = Thresholding()
        self.transform = PerspectiveTransformation()
        self.lanelines = LaneLines()

    def forward(self, img):
        out_img = np.copy(img)
        # Ensure consistent data type (float32)
        if img.dtype != np.float32:
            img = img.astype(np.float32)
        if out_img.dtype != np.float32:
            out_img = out_img.astype(np.float32)
        
        img = self.calibration.undistort(img)
        img = self.transform.forward(img)
        img = self.thresholding.forward(img)
        img = self.lanelines.forward(img)
        img = self.transform.backward(img)

        # Ensure both arrays are same type before addWeighted
        if img.dtype != out_img.dtype:
            img = img.astype(out_img.dtype)
        
        out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
        out_img = self.lanelines.plot(out_img)
        return out_img

    def process_image(self, input_path, output_path):
        img = mpimg.imread(input_path)
        out_img = self.forward(img)
        mpimg.imsave(output_path, out_img)

    def process_video(self, input_path, output_path, display=True):
        if HAS_MOVIEPY:
            # Use moviepy if available
            from moviepy.editor import VideoFileClip
            clip = VideoFileClip(input_path)
            out_clip = clip.fl_image(self.forward)
            out_clip.write_videofile(output_path, audio=False)
        else:
            # Fallback to OpenCV
            print("Using OpenCV for video processing...")
            cap = cv2.VideoCapture(input_path)
            
            if not cap.isOpened():
                raise ValueError(f"Cannot open video file: {input_path}")
            
            # Get video properties
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Define codec and create video writer
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            if not out.isOpened():
                raise ValueError(f"Cannot create output video: {output_path}")
            
            frame_count = 0
            print(f"Processing {total_frames} frames...")
            print("Press 'Q' to quit real-time display\n")
            
            try:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Convert BGR to RGB for processing
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    # Normalize to 0-1 range for processing
                    frame_normalized = frame_rgb.astype(np.float32) / 255.0
                    
                    # Process frame
                    processed = self.forward(frame_normalized)
                    
                    # Convert to uint8 (0-255 range)
                    if processed.dtype == np.float32 or processed.dtype == np.float64:
                        processed = (np.clip(processed, 0, 1) * 255).astype(np.uint8)
                    else:
                        processed = np.clip(processed, 0, 255).astype(np.uint8)
                    
                    # Convert back to BGR for writing
                    if len(processed.shape) == 3 and processed.shape[2] == 3:
                        processed_bgr = cv2.cvtColor(processed, cv2.COLOR_RGB2BGR)
                    else:
                        processed_bgr = processed
                    
                    # Write frame
                    out.write(processed_bgr)
                    
                    # Display frame in real-time if enabled
                    if display:
                        # Resize for display if needed
                        display_frame = processed_bgr
                        if display_frame.shape[1] > 1280:  # Resize if too wide
                            scale = 1280 / display_frame.shape[1]
                            display_frame = cv2.resize(display_frame, None, fx=scale, fy=scale)
                        
                        # Add progress text
                        cv2.putText(display_frame, f"Frame: {frame_count+1}/{total_frames}", 
                                  (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(display_frame, f"Progress: {(frame_count+1)*100/total_frames:.1f}%", 
                                  (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        
                        cv2.imshow("Lane Detection - Real-time Processing", display_frame)
                        
                        # Press 'Q' to skip real-time display
                        key = cv2.waitKey(1) & 0xFF
                        if key == ord('q') or key == ord('Q'):
                            display = False
                            cv2.destroyAllWindows()
                    
                    frame_count += 1
                    if frame_count % 30 == 0:
                        print(f"Processed {frame_count}/{total_frames} frames")
            except Exception as e:
                print(f"Error processing video: {e}")
                raise
            finally:
                cap.release()
                out.release()
                if display:
                    cv2.destroyAllWindows()
                print(f"Video processing complete. Saved to: {output_path}")

def main():
    try:
        args = docopt(__doc__)
        input = args['INPUT_PATH']
        output = args['OUTPUT_PATH']
    except SystemExit:
        # Use defaults if no arguments provided
        input = 'test_images/straight_lines1.jpg'
        output = 'output_videos/output.jpg'
        args = {'--video': False}

    findLaneLines = FindLaneLines()
    if args['--video']:
        findLaneLines.process_video(input, output, display=True)  # Always display in real-time
    else:
        findLaneLines.process_image(input, output)
        print(f"Output saved to: {output}")


if __name__ == "__main__":
    main()
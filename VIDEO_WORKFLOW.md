# Lane Detection - Full Video Processing Workflow

## Pipeline Overview

The video processing pipeline applies the following steps to each frame:

```
Input Video Frame
    ↓
[1] Camera Calibration & Undistortion
    - Removes lens distortion using calibration images
    - Corrects radial and tangential distortion
    ↓
[2] Perspective Transformation (Bird's Eye View)
    - Transforms road view to top-down perspective
    - Makes lane lines appear parallel
    ↓
[3] Thresholding
    - Converts to HSV color space
    - Applies gradient and color thresholding
    - Isolates lane line pixels
    ↓
[4] Lane Detection
    - Uses sliding window technique
    - Detects left and right lane lines
    - Fits polynomial curves to lane pixels
    - Calculates lane curvature and vehicle position
    ↓
[5] Perspective Transform (Inverse)
    - Transforms back to original perspective
    - Overlays detected lanes on original image
    ↓
[6] Output Visualization
    - Draws lane boundaries
    - Displays lane curvature info
    - Highlights detected lane area
    ↓
Output Frame with Lane Detection
```

## How to Run Video Processing

### Option 1: Process a single video with command
```powershell
python main.py --video "project_video.mp4" "output_videos/project_video_output.mp4"
```

### Option 2: Use the demo script
```powershell
python demo_video.py
```

### Option 3: Process with custom parameters
```powershell
python main.py --video "challenge_video.mp4" "output_videos/challenge_output.mp4"
python main.py --video "harder_challenge_video.mp4" "output_videos/harder_challenge_output.mp4"
```

## Available Videos

1. **project_video.mp4** - Main test video
2. **challenge_video.mp4** - Challenge video with shadows
3. **harder_challenge_video.mp4** - Harder challenge with extreme conditions

## Performance

- **Processing speed**: ~2-3 minutes per minute of video (depends on resolution)
- **Output format**: MP4 video with detected lanes overlaid
- **Frame-by-frame processing**: Each frame goes through the complete pipeline

## Output Features

The processed video shows:
- **Green shaded area**: Detected lane region
- **Red/Yellow lines**: Fitted lane boundaries
- **Lane curvature**: Radius of curvature (in meters)
- **Vehicle position**: Offset from center of lane

## Steps in Detail

### 1. Camera Calibration
- Uses chessboard images to calibrate camera
- Computes camera matrix and distortion coefficients
- Applied to every frame to remove lens distortion

### 2. Perspective Transformation
- Selects 4 points on road in original image
- Maps them to rectangular bird's-eye view
- Makes parallel lane lines appear parallel

### 3. Color & Gradient Thresholding
- HSV color space for yellow and white lane lines
- Sobel gradients for edge detection
- Combined thresholding to isolate lane pixels

### 4. Lane Line Detection
- Sliding window algorithm from bottom to top
- Identifies left and right lane pixels
- Fits 2nd order polynomial to each lane

### 5. Lane Curvature Calculation
- Calculates radius of curvature in meters
- Computes vehicle position relative to lane center

## Example Output

After processing:
```
output_videos/project_video_output.mp4 - Processed video
output_videos/challenge_video_output.mp4 - Processed video
output_videos/harder_challenge_video_output.mp4 - Processed video
```

To view the output videos, double-click the files in the output_videos folder!

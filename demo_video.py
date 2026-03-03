"""
Demo script showing the full video processing workflow
"""

import sys
from main import FindLaneLines

def process_video_demo(input_video, output_video):
    """Process video with lane detection"""
    print("=" * 60)
    print("Lane Detection Video Processing")
    print("=" * 60)
    
    # Initialize the lane detection pipeline
    print("\n1. Initializing lane detection pipeline...")
    print("   - Loading camera calibration data")
    print("   - Setting up perspective transformation")
    print("   - Initializing thresholding and lane detection")
    
    findLaneLines = FindLaneLines()
    print("   ✓ Pipeline initialized successfully")
    
    # Process video
    print(f"\n2. Processing video: {input_video}")
    print("   Processing frames with lane detection...")
    
    findLaneLines.process_video(input_video, output_video)
    
    print(f"\n3. Video processing complete!")
    print(f"   Output saved to: {output_video}")
    print("=" * 60)

if __name__ == "__main__":
    # Default video files
    videos = [
        ("project_video.mp4", "output_videos/project_video_output.mp4"),
        ("challenge_video.mp4", "output_videos/challenge_video_output.mp4"),
        ("harder_challenge_video.mp4", "output_videos/harder_challenge_video_output.mp4"),
    ]
    
    print("\nAvailable videos:")
    for i, (input_vid, output_vid) in enumerate(videos, 1):
        print(f"  {i}. {input_vid}")
    
    # Process the first video as demo
    input_video = "project_video.mp4"
    output_video = "output_videos/project_video_output.mp4"
    
    print(f"\nProcessing: {input_video}")
    print("This may take a few minutes...\n")
    
    try:
        process_video_demo(input_video, output_video)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

"""
Real-time Lane Detection Video Processor
Automatically processes videos with live display
"""

import os
import sys
from main import FindLaneLines

def run_realtime(video_file=None, output_file=None):
    """Run video processing with real-time display"""
    
    # Default to project_video.mp4 if not specified
    if video_file is None:
        video_file = "project_video.mp4"
    
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(video_file))[0]
        output_file = f"output_videos/{base_name}_processed.mp4"
    
    # Check if video exists
    if not os.path.exists(video_file):
        print(f"Error: Video file '{video_file}' not found!")
        print("\nAvailable videos:")
        for vid in ["project_video.mp4", "challenge_video.mp4", "harder_challenge_video.mp4"]:
            if os.path.exists(vid):
                print(f"  - {vid}")
        return
    
    print("="*60)
    print("LANE DETECTION - REAL-TIME VIDEO PROCESSOR")
    print("="*60)
    print(f"\nInput Video:  {video_file}")
    print(f"Output Video: {output_file}")
    print("\nProcessing with real-time display...")
    print("Press 'Q' during playback to close display window\n")
    
    try:
        findLaneLines = FindLaneLines()
        findLaneLines.process_video(video_file, output_file, display=True)
        
        print("\n" + "="*60)
        print("SUCCESS! Video processing complete!")
        print(f"Output saved to: {output_file}")
        print("="*60)
        
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        video = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else None
        run_realtime(video, output)
    else:
        # Run with default settings
        run_realtime()

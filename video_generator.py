#pip install opencv-python
#winget install ffmpeg


import cv2
import numpy as np
import os
import ffmpeg

def detect_transitions(video_path, threshold=30):
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    frame_diffs = []
    transition_frames = []
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray)
            mean_diff = np.mean(diff)
            frame_diffs.append(mean_diff)
            
            if mean_diff > threshold:
                transition_frames.append(frame_count)
        
        prev_frame = gray
        frame_count += 1
    
    cap.release()
    return transition_frames

def split_video(video_path, transition_frames, output_folder, segment_duration=3):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    transition_frames.append(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))  # Ensure last frame is included
    
    start_frame = 0
    for i, end_frame in enumerate(transition_frames):
        segment_start_time = start_frame / fps
        segment_end_time = min(segment_start_time + segment_duration, end_frame / fps)
        
        output_file = os.path.join(output_folder, f'segment_{i+1}.mp4')
        (
            ffmpeg
            .input(video_path, ss=segment_start_time, to=segment_end_time)
            .output(output_file, vcodec='libx264', acodec='aac')
            .run(overwrite_output=True, quiet=True)
        )
        
        start_frame = end_frame

def main():
    video_path = "D:\ChanaTV\levelup\1.ts"  # 修改为你的输入视频文件
    output_folder = 'output_segments'
    
    print("Detecting transitions...")
    transitions = detect_transitions(video_path)
    print(f"Detected {len(transitions)} transitions at frames: {transitions}")
    
    print("Splitting video...")
    split_video(video_path, transitions, output_folder)
    print(f"Segments saved in {output_folder}")

if __name__ == "__main__":
    main()

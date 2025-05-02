from moviepy.editor import VideoFileClip, concatenate_videoclips
import math
import os

def cut_video(input_path, output_path, desired_duration, start_time, end_time):
    """
    Cut video by keeping 3-second segments and removing calculated intervals.
    
    Args:
        input_path (str): Path to the input video file
        output_path (str): Path where the output video will be saved
        desired_duration (float): Desired duration of the output video in seconds
    """
    # Load the video
    video = VideoFileClip(input_path)
    original_duration = video.duration

    if end_time < original_duration:
        print("update original_duration=", original_duration, " by end_time=", end_time)
        original_duration = end_time
    
    # Calculate the number of 3-second segments we can keep
    keep_duration = 3  # seconds per kept segment
    total_removed_duration = original_duration - desired_duration
    
    # Calculate how many complete 3-second segments we can fit
    # num_segments = math.floor(desired_duration / keep_duration)
    num_segments = math.ceil(desired_duration / keep_duration)
    
    # Calculate the duration to remove between each kept segment
    remove_duration = total_removed_duration / (num_segments - 1) if num_segments > 1 else 0
    
    # Create clips list
    clips = []
    current_time = start_time
    
    for i in range(num_segments):
        if current_time + keep_duration > original_duration:
            break
            
        # Extract 3-second clip
        clip = video.subclip(current_time, current_time + keep_duration)
        clips.append(clip)
        
        # Move to next position (skip the removal duration)
        current_time += keep_duration + remove_duration
    
    # Concatenate all clips
    final_video = concatenate_videoclips(clips)
    
    # Write the output video
    final_video.write_videofile(output_path)
    
    # Close all clips
    final_video.close()
    for clip in clips:
        clip.close()
    video.close()

# Example usage:
if __name__ == "__main__":
    # Example parameters
    cwd = os.getcwd()
    input_video = cwd + '/'+ 'pokemon1.mp4'
    output_video = cwd + '/'+ 'output.mp4'
    target_duration = 30  # desired duration in seconds
    
    cut_video(input_video, output_video, target_duration, 50, 3600) 
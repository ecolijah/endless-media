import os
import subprocess
import random

# Directory containing the video files
video_directory = "/home/gth/endless-media-files"

# Function to get a list of video files in the directory
def get_video_files(directory):
    video_files = [f for f in os.listdir(directory) if f.endswith((".mp4", ".avi", ".mkv"))]
    random.shuffle(video_files)
    return (video_files)  # Sort the files for playback order

# Function to play videos continuously
def play_videos(video_files):
    for video_file in video_files:
        # Launch VLC with the current video file and wait for it to finish
        print("playing: " +  str(video_file))
        subprocess.run(["vlc", "--fullscreen","--play-and-exit", os.path.join(video_directory, video_file)])

# Main function
def main():
    
    while True:
        video_files = get_video_files(video_directory)
        print("files to be played in this order: ")
        for file in video_files:
            print(file)
        play_videos(video_files)

if __name__ == "__main__":
    main()

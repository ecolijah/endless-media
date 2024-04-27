import os
import subprocess
import random


# function reads every line of txt file into list as an element.
def read_file_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())  # Remove leading/trailing whitespace
    random.shuffle(lines)
    return lines

# Function to play videos continuously
def play_videos(video_urls):
        
    for video in video_urls:
        print("playing: " +  str(video))
        subprocess.run(["vlc", "--fullscreen","--play-and-exit", video])

# Main function
def main():
    
    while True:
        video_urls = read_file_lines("youtube_urls.txt")
        play_videos(video_urls)

if __name__ == "__main__":
    main()

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import os

# Function to extract captions and save them in a text file
def extract_english_captions(youtube_url):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)
        
        # Extract video title and use it for the filename
        video_title = yt.title
        sanitized_title = ''.join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        file_name = f"{sanitized_title}.txt"
        
        # Get the video ID from the URL
        video_id = yt.video_id
        
        # Fetch English captions (subtitles)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Open the text file to write captions
        with open(file_name, 'w', encoding='utf-8') as f:
            for entry in transcript:
                f.write(f"{entry['text']}\n")
        
        print(f"Captions extracted and saved to '{file_name}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
youtube_url = input("Enter the YouTube video URL: ")
extract_english_captions(youtube_url)

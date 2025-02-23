from pytube import YouTube

def download_youtube_video(video_url, save_path):
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # # Display video details
        # print("Title:", yt.title)
        # print("Views:", yt.views)
        # print("Duration (s):", yt.length)
        # print("Author:", yt.author)
        
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print("Downloading...")
        video_stream.download(output_path=save_path)
        print(f"Downloaded successfully! Saved to {save_path}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("YouTube Video Downloader")
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path to save the video (e.g., C:/Users/YourName/Downloads): ")
    download_youtube_video(video_url, save_path)

import yt_dlp

def download_multiple_videos(video_urls, save_path, quality):
   
    quality_options = {
        '1': 'best',          
        '2': 'bestvideo+bestaudio',  
        '3': 'worst',        
        '4': 'bestaudio',    
        '5': 'worstvideo'    
    }

    selected_format = quality_options.get(quality, 'best')

    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': selected_format,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for url in video_urls:
                print(f"Downloading: {url} in {selected_format} quality")
                ydl.download([url])
        print("All videos downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


print("Enter the YouTube video URLs (enter 'done' to stop):")
video_urls = []
while True:
    url = input("Enter YouTube video URL: ")
    if url.lower() == 'done':
        break
    video_urls.append(url)


save_path = input("Enter the path to save the videos (e.g., D:/BTECH/PPS_Compl): ")


print("\nSelect Video Quality:")
print("1: Best Quality (Default)")
print("2: Best Video + Best Audio")
print("3: Lowest Quality")
print("4: Audio Only")
print("5: Lowest Video Quality")
quality = input("Enter your choice (1-5): ")


download_multiple_videos(video_urls, save_path, quality)

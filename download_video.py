from pytube import YouTube
import os

def download_video(url, output_path="."):
    try:
        yt = YouTube(url)

        print(f"Title: {yt.title}")
        print(f"Duration: {yt.length} seconds")
        print(f"Views: {yt.views}")

        video = yt.streams.get_highest_resolution()
        print("Downloading...")
        video.download(output_path)
        print(f"Download completed! File saved in {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (press Enter for current directory): ")

    if not download_path:
        download_path = "."

    download_video(video_url, download_path)

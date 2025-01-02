import requests
from bs4 import BeautifulSoup

def extract_video_id(url):
    """Extract the video ID from a YouTube live stream URL."""
    if "youtube.com" in url:
        # Look for the "v=" parameter in the URL to extract the video ID
        video_id = url.split("v=")[-1].split("&")[0]
        return video_id
    return None

def get_m3u8_url(video_id):
    """Generate a valid m3u8 URL for a YouTube live stream."""
    m3u8_url = f"https://www.youtube.com/watch?v={video_id}"
    return m3u8_url

def generate_m3u_playlist(urls):
    """Generate an M3U playlist from a list of YouTube live URLs."""
    m3u_playlist = "#EXTM3U\n"
    
    for index, url in enumerate(urls, 1):
        video_id = extract_video_id(url)
        if video_id:
            m3u8_url = get_m3u8_url(video_id)
            m3u_playlist += f"#EXTINF:-1,Stream {index} - {url}\n{m3u8_url}\n"
        else:
            print(f"Error: Invalid YouTube URL {url}")
    
    return m3u_playlist

def save_m3u_playlist(playlist_content, filename="playlist.m3u"):
    """Save the generated M3U playlist to a file."""
    with open(filename, "w") as file:
        file.write(playlist_content)

def main():
    # Replace this list with your actual YouTube live URLs
    youtube_urls = [
        "https://www.youtube.com/@somoynews360/live",
        "https://www.youtube.com/@JamunaTVbd/live",
        "https://www.youtube.com/@channel24digital/live",
        "https://www.youtube.com/@dbcnewstv/live",
        "https://www.youtube.com/@ATNNews24/live",
        "https://www.youtube.com/@ChanneliNews/live",
        "https://www.youtube.com/@IndependentTelevision/live",
        "https://www.youtube.com/@EkattorTelevision/live",
        "https://www.youtube.com/@RtvNews/live",
        "https://www.youtube.com/@ekhontv/live",
        "https://www.youtube.com/@news24television90/live",
        "https://www.youtube.com/@NTVDigitalLive/live",
        "https://www.youtube.com/@livedeshtv/live"
    ]
    
    # Generate M3U playlist
    playlist_content = generate_m3u_playlist(youtube_urls)
    
    # Save playlist to a file
    save_m3u_playlist(playlist_content)

if __name__ == "__main__":
    main()

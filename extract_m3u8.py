import yt_dlp

def extract_m3u8_url(youtube_url):
    """Use yt-dlp to extract the M3U8 URL from a YouTube live stream URL."""
    ydl_opts = {
        'quiet': True, 
        'format': 'best', 
        'noplaylist': True, 
        'extract_flat': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        if 'formats' in info_dict:
            for format_info in info_dict['formats']:
                if 'm3u8' in format_info['url']:
                    return format_info['url']
    return None

def generate_m3u_playlist(urls):
    """Generate an M3U playlist from a list of YouTube live URLs."""
    m3u_playlist = "#EXTM3U\n"
    
    for index, url in enumerate(urls, 1):
        m3u8_url = extract_m3u8_url(url)
        if m3u8_url:
            m3u_playlist += f"#EXTINF:-1,Stream {index} - {url}\n{m3u8_url}\n"
        else:
            print(f"Error: Could not extract M3U8 URL from {url}")
    
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

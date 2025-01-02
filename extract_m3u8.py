import subprocess
import json
import requests

# Input and output files
URL_FILE = "channels.txt"
OUTPUT_FILE = "m3u8_links.txt"

# Resolve redirected URLs
def resolve_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return response.url
    except Exception as e:
        print(f"Error resolving URL {url}: {e}")
        return url

# Fetch the m3u8 URL using yt-dlp with cookies
def get_m3u8_url(youtube_url):
    try:
        result = subprocess.run(
            ["yt-dlp", "-j", "--cookies", "cookies.txt", youtube_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error fetching video info for {youtube_url}: {result.stderr}")
            return None

        video_info = json.loads(result.stdout)
        formats = video_info.get("formats", [])

        # Debugging: Print available formats
        print(f"Formats for {youtube_url}:")
        for fmt in formats:
            print(fmt)

        # Extract the .m3u8 URL
        for fmt in formats:
            if "m3u8" in fmt.get("url", ""):
                return fmt["url"]

        print(f"No .m3u8 URL found for {youtube_url}.")
        return None
    except Exception as e:
        print(f"Error processing {youtube_url}: {e}")
        return None

# Process all channels from the input file
def process_channels():
    try:
        with open(URL_FILE, "r") as file:
            channels = file.readlines()

        with open(OUTPUT_FILE, "w") as output_file:
            for channel in channels:
                youtube_url = resolve_url(channel.strip())
                if youtube_url:
                    print(f"Processing {youtube_url}...")
                    m3u8_url = get_m3u8_url(youtube_url)
                    if m3u8_url:
                        print(f"Found M3U8 URL for {youtube_url}: {m3u8_url}")
                        output_file.write(f"{youtube_url} -> {m3u8_url}\n")
    except FileNotFoundError:
        print(f"Error: {URL_FILE} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main entry point
if __name__ == "__main__":
    process_channels()

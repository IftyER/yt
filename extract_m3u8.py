input_file = "channels.txt"
output_file = "m3u8_links.m3u"

# Read the links from channels.txt
with open(input_file, "r") as file:
    m3u8_links = [line.strip() for line in file if line.strip()]  # Strip whitespace and skip empty lines

# Write links to the m3u file
with open(output_file, "w") as file:
    # Add the M3U file header
    file.write("#EXTM3U\n")
    
    for i, link in enumerate(m3u8_links, start=1):
        # Add metadata for each link
        file.write(f"#EXTINF:-1,Stream {i}\n")
        file.write(f"{link}\n")

print(f"{len(m3u8_links)} links have been saved to {output_file}.")

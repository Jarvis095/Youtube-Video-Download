# YouTube Video Downloader

A simple and powerful Python script for downloading YouTube videos using yt-dlp with custom FFmpeg support.

## Features

- Download videos in various qualities (best, worst, or specific resolutions like 720p, 1080p)
- Support for multiple output formats (mp4, mkv, webm, etc.)
- Audio-only download mode (converts to MP3)
- Custom FFmpeg path support
- Progress tracking during download
- Automatic video information display (title, duration, views)

## Prerequisites

- Python 3.6 or higher
- yt-dlp library
- FFmpeg (recommended for best results)

## Installation

1. Install Python dependencies:
```bash
pip install yt-dlp
```

2. Install FFmpeg (highly recommended):
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Ubuntu/Debian) or `sudo yum install ffmpeg` (CentOS/RHEL)

3. Download the script and make it executable (Linux/macOS):
```bash
chmod +x youtube_downloader.py
```

## Usage

### Basic Usage

Download a video with default settings (best quality, MP4 format):
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Advanced Options

**Specify output directory:**
```bash
python youtube_downloader.py "URL" -o /path/to/downloads
```

**Choose video quality:**
```bash
python youtube_downloader.py "URL" -q 720
python youtube_downloader.py "URL" -q 1080
python youtube_downloader.py "URL" -q best
python youtube_downloader.py "URL" -q worst
```

**Select output format:**
```bash
python youtube_downloader.py "URL" -f mkv
python youtube_downloader.py "URL" -f webm
```

**Download audio only (MP3):**
```bash
python youtube_downloader.py "URL" -a
```

**Specify custom FFmpeg path:**
```bash
python youtube_downloader.py "URL" --ffmpeg-path /path/to/ffmpeg
python youtube_downloader.py "URL" --ffmpeg-path "C:\ffmpeg\bin\ffmpeg.exe"
```

### Combined Options

```bash
python youtube_downloader.py "URL" -o ./videos -q 1080 -f mp4 --ffmpeg-path /usr/local/bin/ffmpeg
```

## Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `url` | - | YouTube video URL (required) | - |
| `--output` | `-o` | Output directory | `./downloads` |
| `--quality` | `-q` | Video quality (best, worst, 720, 1080, etc.) | `best` |
| `--format` | `-f` | Output format (mp4, mkv, webm, etc.) | `mp4` |
| `--audio-only` | `-a` | Download audio only as MP3 | `False` |
| `--ffmpeg-path` | - | Custom path to FFmpeg executable or directory | `None` |

## Examples

1. **Download best quality video:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

2. **Download 720p video to specific folder:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o ~/Videos -q 720
```

3. **Extract audio as MP3:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a
```

4. **Download with custom FFmpeg:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --ffmpeg-path "C:\Tools\ffmpeg\bin"
```

## Troubleshooting

### FFmpeg Not Found

If you see a warning about FFmpeg not being found:
1. Install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Add FFmpeg to your system PATH, or
3. Use the `--ffmpeg-path` option to specify its location

### Download Errors

- Ensure the YouTube URL is valid and accessible
- Check your internet connection
- Some videos may be restricted by region or require authentication
- Update yt-dlp: `pip install --upgrade yt-dlp`

### Permission Errors

Make sure you have write permissions in the output directory.

## Notes

- The script automatically creates the output directory if it doesn't exist
- Downloaded files are named after the video title
- Progress information is displayed during download
- FFmpeg is required for merging video and audio streams and for audio extraction

## Legal Disclaimer

This tool is for personal use only. Respect copyright laws and YouTube's Terms of Service. Only download videos you have permission to download.

## License

This project is provided as-is for educational purposes.

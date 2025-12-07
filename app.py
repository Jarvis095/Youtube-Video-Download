#!/usr/bin/env python3
import yt_dlp
import argparse
import os
import sys
import subprocess

def check_ffmpeg(custom_path=None):
    """
    Check if FFmpeg is installed, with optional custom path.
    """
    try:
        if custom_path:
            # Check if the custom path points directly to ffmpeg.exe
            if os.path.isfile(custom_path):
                ffmpeg_path = custom_path
            # Or if it's a directory containing ffmpeg.exe
            elif os.path.isdir(custom_path):
                ffmpeg_path = os.path.join(custom_path, 'ffmpeg.exe')
            else:
                return False
            
            subprocess.run([ffmpeg_path, '-version'], 
                         stdout=subprocess.DEVNULL, 
                         stderr=subprocess.DEVNULL,
                         check=True)
            return ffmpeg_path
        else:
            # Check system PATH
            subprocess.run(['ffmpeg', '-version'], 
                          stdout=subprocess.DEVNULL, 
                          stderr=subprocess.DEVNULL,
                          check=True)
            return 'ffmpeg'
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def download_video(url, output_path='./downloads', quality='best', format='mp4', audio_only=False, ffmpeg_path=None):
    """
    Download a YouTube video using yt-dlp with custom FFmpeg support.
    """
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'progress_hooks': [progress_hook],
        'merge_output_format': format,
    }
    
    # Check for FFmpeg
    ffmpeg_location = check_ffmpeg(ffmpeg_path)
    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location
        print(f"\nUsing FFmpeg at: {ffmpeg_location}")
    else:
        print("\nWARNING: FFmpeg not found. Some videos may not process correctly.")
        print("For best results, install FFmpeg and add it to your PATH or specify its location with --ffmpeg-path")
        print("Download from: https://ffmpeg.org/download.html\n")
    
    # Format selection
    if audio_only:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        if quality == 'best':
            ydl_opts['format'] = f'bestvideo[ext={format}]+bestaudio/best'
        elif quality == 'worst':
            ydl_opts['format'] = 'worst'
        else:
            ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best'
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"\nDownloading: {info.get('title', 'Unknown Title')}")
            print(f"Duration: {info.get('duration', 'Unknown')} seconds")
            print(f"Views: {info.get('view_count', 'Unknown')}")
            
            ydl.download([url])
        print("\nDownload completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(f"\nDownload error: {e}")
        if "ffmpeg" in str(e).lower():
            print("\nFFmpeg is required for proper processing of this video.")
            if ffmpeg_path:
                print(f"The specified FFmpeg path ({ffmpeg_path}) may be incorrect.")
            print("Please verify your FFmpeg installation at https://ffmpeg.org/download.html")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} of ~{d['_total_bytes_estimate_str']} at {d['_speed_str']}", end='')
    elif d['status'] == 'finished':
        print("\nProcessing video...")

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Downloader with FFmpeg support')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-o', '--output', default='./downloads', help='Output directory (default: ./downloads)')
    parser.add_argument('-q', '--quality', default='best', 
                        help='Video quality (best, worst, or specific like 720p, 1080p)')
    parser.add_argument('-f', '--format', default='mp4', 
                        help='Output format (mp4, mkv, webm, etc.)')
    parser.add_argument('-a', '--audio-only', action='store_true', 
                        help='Download audio only (MP3)')
    parser.add_argument('--ffmpeg-path', default=None,
                        help='Custom path to FFmpeg executable or directory containing ffmpeg')
    
    args = parser.parse_args()
    
    print("Starting download...")
    download_video(
        args.url,
        output_path=args.output,
        quality=args.quality,
        format=args.format,
        audio_only=args.audio_only,
        ffmpeg_path=args.ffmpeg_path
    )

if __name__ == '__main__':
    main()

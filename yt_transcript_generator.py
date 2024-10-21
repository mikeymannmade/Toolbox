import os
from pytube import YouTube
import subprocess
import whisper
import json

def download_video_extract_audio(youtube_url, base_output_folder):
    yt = YouTube(youtube_url)
    video_title = yt.title.replace('"', '').replace('|', '').replace('?', '').replace('*', '')  # Remove problematic characters
    video_title = ''.join(i for i in video_title if i not in "\/:*?<>|")  # Further clean up for Windows file naming
    output_folder = os.path.join(base_output_folder, video_title)
    os.makedirs(output_folder, exist_ok=True)
    audio_stream = yt.streams.get_audio_only()
    audio_file_path = audio_stream.download(output_path=output_folder)
    return audio_file_path, output_folder

def convert_to_mp3(audio_file_path, output_folder):
    mp3_file_path = os.path.splitext(audio_file_path)[0] + '.mp3'
    subprocess.run(f'ffmpeg -i "{audio_file_path}" -vn -ab 128k -ar 44100 "{mp3_file_path}"', shell=True)
    os.remove(audio_file_path)  # Remove the original MP4 file
    return mp3_file_path

def transcribe_audio(model_name, audio_file_path, output_folder):
    model = whisper.load_model("medium")
    result = model.transcribe(audio_file_path)
    
    output_files = {}

    # Save the transcript text
    text_file_path = os.path.splitext(audio_file_path)[0] + '.txt'
    with open(text_file_path, 'w', encoding='utf-8') as f:
        f.write(result['text'])
    output_files['text'] = text_file_path

    # Save the segments as JSON
    if 'segments' in result:
        json_file_path = os.path.splitext(audio_file_path)[0] + '.json'
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(result['segments'], f, ensure_ascii=False, indent=4)
        output_files['json'] = json_file_path

    # Check if 'srt' is in the result and save it
    if 'srt' in result:
        srt_file_path = os.path.splitext(audio_file_path)[0] + '.srt'
        with open(srt_file_path, 'w', encoding='utf-8') as f:
            f.write(result['srt'])
        output_files['srt'] = srt_file_path

    # Check if 'vtt' is in the result and save it
    if 'vtt' in result:
        vtt_file_path = os.path.splitext(audio_file_path)[0] + '.vtt'
        with open(vtt_file_path, 'w', encoding='utf-8') as f:
            f.write(result['vtt'])
        output_files['vtt'] = vtt_file_path

    return output_files

def main():
    youtube_url = input("Enter the YouTube video URL: ")
    base_output_folder = "Z:\\Projects\\Whisper"

    print(f"Downloading and extracting audio from {youtube_url}...")
    audio_file_path, output_folder = download_video_extract_audio(youtube_url, base_output_folder)

    print(f"Converting extracted audio to MP3...")
    mp3_file_path = convert_to_mp3(audio_file_path, output_folder)

    print(f"Generating transcript for the audio...")
    transcript_file_path = transcribe_audio("small", mp3_file_path, output_folder)

    print(f"All operations completed. Files are saved in: {output_folder}")

if __name__ == "__main__":
    main()

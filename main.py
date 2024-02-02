

from moviepy.video.io.VideoFileClip import VideoFileClip
# from pydub import AudioSegment
import speech_recognition as sr
import cv2
import pytesseract
from PIL import Image
import os

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    # audio = AudioSegment.from_file(audio_path)

    with sr.AudioFile(audio_path) as source:
        audio_data = r.listen(source)

    transcript = r.recognize_google(audio_data)
    # print(transcript)
    return transcript

def generate_short_clip(video_path, output_clip_path, start_time, end_time):
    with VideoFileClip(video_path) as video:
        subclip = video.subclip(start_time, end_time)
        subclip.write_videofile(output_clip_path, codec='libx264', audio_codec='aac')

# Rest of your code remains unchanged
def ai_short_clipper(video_path, output_folder, topic):
    # Step 1: Extract audio from the video
    audio_path = os.path.join(output_folder, "audio.wav")
    extract_audio(video_path, audio_path)

    # Step 2: Transcribe the audio
    transcript = transcribe_audio(audio_path)
    # print("Transcript:", transcript)

    # Step 3: Find all occurrences of the topic in the transcript
    start_times = [pos for pos in range(len(transcript)) if transcript.startswith(topic, pos)]
    print(start_times)
    print("=========================")
    # If the keyword is not found, print a message and exit
    if not start_times:
        print(f"Keyword '{topic}' not found in the transcript.")
        return

    # Use the start time of the first occurrence as a reference
    reference_start_time = start_times[0]

    # Step 4: Generate short clips based on relevant time ranges
    for start_time in start_times:
        end_time = start_time + len(topic)

        # Adjust start time to be consistent with the reference
        adjusted_start_time = start_time - (reference_start_time - 0)

        output_clip_path = os.path.join(output_folder, f"output_clip_{adjusted_start_time}.mp4")
        generate_short_clip(video_path, output_clip_path, adjusted_start_time, end_time)  # No need to add extra seconds here

if __name__ == "__main__":
    input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
    output_clip_folder = r"C:\Users\Zein\Desktop\New folder\test"
    specific_topic = "bones are strong"

    ai_short_clipper(input_video_path, output_clip_folder, specific_topic)

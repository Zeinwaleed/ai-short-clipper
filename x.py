
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
import speech_recognition as sr
import cv2
import pytesseract
from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor
import threading

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)

    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)

    transcript = r.recognize_google(audio_data)
    return transcript

def extract_text_from_frames(video_path, text_result, frame_sampling_rate=10):
    video = cv2.VideoCapture(video_path)
    text = ""
    frame_count = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break

        if frame_count % frame_sampling_rate == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text += pytesseract.image_to_string(Image.fromarray(gray))

        frame_count += 1

    video.release()
    text_result.append(text)

def generate_short_clip(video_path, output_clip_path, start_time, end_time):
    video = VideoFileClip(video_path)
    subclip = video.subclip(start_time, end_time)
    subclip.write_videofile(output_clip_path, codec='libx264', audio_codec='aac')

def ai_short_clipper(video_path, output_folder, topic):
    # Step 1: Extract audio from the video
    audio_path = os.path.join(output_folder, "audio.wav")

    with ThreadPoolExecutor() as executor:
        audio_future = executor.submit(extract_audio, video_path, audio_path)
        text_result = []
        text_future = executor.submit(extract_text_from_frames, video_path, text_result)

        # Wait for both tasks to complete
        audio_future.result()
        text_future.result()

    # Step 2: Transcribe the audio
    transcript = transcribe_audio(audio_path)
    print("Transcript:", transcript)

    # Step 3: Extract text from video frames
    video_text = text_result[0]
    print("Extracted Text from Video:", video_text)

    # Step 4: Find the relevant time range based on the specified topic
    start_time_index = transcript.find(topic)

    # If the keyword is not found, print a message and exit
    if start_time_index == -1:
        print(f"Keyword '{topic}' not found in the transcript.")
        return

    # Calculate start and end times in seconds based on characters
    start_time = transcript[:start_time_index].count(' ')
    end_time = start_time + len(topic)  # Adjust this based on your specific requirements

    # Step 5: Generate short clip based on relevant time range
    output_clip_path = os.path.join(output_folder, "output_clip.mp4")
    generate_short_clip(video_path, output_clip_path, start_time, end_time + 10)  # Add 10 seconds for context


if __name__ == "__main__":
    input_video_path = r"C:\Users\Zein\Desktop\New folder\test.mp4"
    output_clip_folder = r"C:\Users\Zein\Desktop\New folder\test"
    specific_topic = "seasoned"

    ai_short_clipper(input_video_path, output_clip_folder, specific_topic)

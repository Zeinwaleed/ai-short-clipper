# from moviepy.video.io.VideoFileClip import VideoFileClip
# from pydub import AudioSegment
# import speech_recognition as sr
# import cv2
# import pytesseract
# from PIL import Image
# import os

# def extract_audio(video_path, audio_path):
#     video = VideoFileClip(video_path)
#     audio = video.audio
#     audio.write_audiofile(audio_path)

# def transcribe_audio(audio_path):
#     r = sr.Recognizer()
#     audio = AudioSegment.from_file(audio_path)

#     with sr.AudioFile(audio_path) as source:
#         audio_data = r.record(source)

#     transcript = r.recognize_google(audio_data)
#     return transcript

# def extract_text_from_frames(video_path):
#     video = cv2.VideoCapture(video_path)
#     text = ""

#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break

#         # Convert the frame to grayscale and extract text using Tesseract
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         text += pytesseract.image_to_string(Image.fromarray(gray))

#     video.release()
#     return text

# def generate_short_clip(video_path, output_clip_path, start_time, end_time):
#     video = VideoFileClip(video_path)
#     subclip = video.subclip(start_time, end_time)
#     subclip.write_videofile(output_clip_path, codec='libx264', audio_codec='aac')

# def ai_short_clipper(video_path, output_folder, topic):
#     # Step 1: Extract audio from the video
#     audio_path = os.path.join(output_folder, "audio.wav")
#     extract_audio(video_path, audio_path)

#     # Step 2: Transcribe the audio
#     transcript = transcribe_audio(audio_path)
#     print("Transcript:", transcript)

#     # Step 3: Extract text from video frames
#     video_text = extract_text_from_frames(video_path)
#     print("Extracted Text from Video:", video_text)

#     # Step 4: Find the relevant time range based on the specified topic
#     start_time = transcript.find(topic)
    
#     # If the keyword is not found, print a message and exit
#     if start_time == -1:
#         print(f"Keyword '{topic}' not found in the transcript.")
#         return

#     end_time = start_time + len(topic)  # You may need to adjust this based on your specific requirements

#     # Step 5: Generate short clip based on relevant time range
#     output_clip_path = os.path.join (output_folder, "output_clip.mp4")
#     generate_short_clip(video_path, output_clip_path, start_time, end_time + 10)  # Add 10 seconds for context




# if __name__ == "__main__":
#     input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
#     output_clip_folder = r"C:\Users\Zein\Desktop\New folder\test"
#     specific_topic = "bone"

#     ai_short_clipper(input_video_path, output_clip_folder, specific_topic)













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













# from moviepy.video.io.VideoFileClip import VideoFileClip
# from pydub import AudioSegment
# import speech_recognition as sr
# import pytesseract
# from PIL import Image
# import os

# def extract_audio(video_path, audio_path):
#     video = VideoFileClip(video_path)
#     audio = video.audio
#     audio.write_audiofile(audio_path)

# def transcribe_audio(audio_path):
#     r = sr.Recognizer()
#     audio = AudioSegment.from_file(audio_path)

#     with sr.AudioFile(audio_path) as source:
#         audio_data = r.record(source)

#     transcript = r.recognize_google(audio_data)
#     return transcript

# def extract_text_from_video(video_path, start_time, end_time):
#     # Load video clip
#     video = VideoFileClip(video_path)

#     # Extract audio from the specified time range
#     audio_clip = video.subclip(start_time, end_time)
#     audio_path = "audio_temp.wav"
#     audio_clip.write_audiofile(audio_path, codec='pcm_s16le')

#     # Transcribe the audio
#     transcript = transcribe_audio(audio_path)
#     print("Transcript:", transcript)

#     # Extract text from video frames in the specified time range
#     video_clip = video.subclip(start_time, end_time)
#     text = ""

#     for frame in video_clip.iter_frames(fps=video.fps):
#         gray = Image.fromarray(frame).convert('L')
#         text += pytesseract.image_to_string(gray)

#     return text

# if __name__ == "__main__":
#     input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
#     output_clip_folder = r"C:\Users\Zein\Desktop\New folder\test"
#     specific_topic = "bone"
#     start_time = 60  # Start time in seconds
#     end_time = 120   # End time in seconds

#     # Step 1: Extract audio from the specified time range
#     audio_path = os.path.join(output_clip_folder, "audio.wav")
#     extract_audio(input_video_path, audio_path)

#     # Step 2: Transcribe the audio
#     transcript = transcribe_audio(audio_path)
#     print("Transcript:", transcript)

#     # Step 3: Extract text from video frames in the specified time range
#     extracted_text = extract_text_from_video(input_video_path, start_time, end_time)
#     print("Extracted Text from Video:", extracted_text)


# if __name__ == "__main__":
#     input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
#     output_clip_folder = r"C:\Users\Zein\Desktop\New folder\test"
#     specific_topic = "bone"

#     ai_short_clipper(input_video_path, output_clip_folder, specific_topic)













# from moviepy.video.io.VideoFileClip import VideoFileClip
# from pydub import AudioSegment
# import speech_recognition as sr
# import pytesseract
# from PIL import Image
# import os
# import re

# def extract_audio(video_path, audio_path):
#     video = VideoFileClip(video_path)
#     audio = video.audio
#     audio.write_audiofile(audio_path)

# def transcribe_audio(audio_path):
#     r = sr.Recognizer()
#     audio = AudioSegment.from_file(audio_path)

#     with sr.AudioFile(audio_path) as source:
#         audio_data = r.record(source)

#     transcript = r.recognize_google(audio_data)
#     return transcript

# def extract_text_from_video(video_path, start_time, end_time):
#     # Load video clip
#     video = VideoFileClip(video_path)

#     # Ensure end_time is not greater than the video duration
#     end_time = min(end_time, video.duration) if end_time is not None else video.duration

#     # Extract audio from the specified time range
#     audio_clip = video.subclip(start_time, end_time)
#     audio_path = "audio_temp.wav"
#     audio_clip.write_audiofile(audio_path, codec='pcm_s16le')

#     # Transcribe the audio
#     transcript = transcribe_audio(audio_path)
#     print("Transcript:", transcript)

#     # Extract text from video frames in the specified time range
#     video_clip = video.subclip(start_time, end_time)
#     text = ""

#     for frame in video_clip.iter_frames(fps=video.fps):
#         gray = Image.fromarray(frame).convert('L')
#         text += pytesseract.image_to_string(gray)

#     return text

# def find_silence_ranges(audio_path, silence_threshold=-40, silence_duration=1000):
#     audio = AudioSegment.from_file(audio_path)
#     silence_ranges = []

#     start_time = 0
#     current_range = None

#     for i, chunk in enumerate(audio[::silence_duration]):
#         if chunk.dBFS < silence_threshold:
#             if current_range is None:
#                 start_time = i * silence_duration
#                 current_range = [start_time, start_time + silence_duration]
#             else:
#                 current_range[1] = (i + 1) * silence_duration
#         elif current_range is not None:
#             silence_ranges.append(tuple(current_range))
#             current_range = None

#     if current_range is not None:
#         silence_ranges.append(tuple(current_range))

#     return silence_ranges

# def cut_video_by_topic_and_silence(video_path, output_folder, specific_topic, silence_threshold=-40, silence_duration=1000):
#     # Extract audio from the entire video
#     extract_audio(video_path, "audio_temp.wav")

#     # Find silence ranges in the audio
#     silence_ranges = find_silence_ranges("audio_temp.wav", silence_threshold, silence_duration)

#     # Cut video segments based on silence ranges and topic occurrence
#     for start_time, end_time in silence_ranges:
#         # Extract text from the silence period
#         text = extract_text_from_video(video_path, start_time / 1000, end_time / 1000)

#         # Check if the specific topic is present in the extracted text
#         if specific_topic.lower() in text.lower():
#             output_clip_path = os.path.join(output_folder, f"clip_{start_time}_{end_time}.mp4")

#             # Generate the short clip
#             video = VideoFileClip(video_path)
#             short_clip = video.subclip(start_time / 1000, end_time / 1000)
#             short_clip.write_videofile(output_clip_path, codec='libx264', audio_codec='aac')

#             print(f"Short clip generated successfully: {output_clip_path}")

# if __name__ == "__main__":
#     input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
#     output_folder =  r"C:\Users\Zein\Desktop\New folder\test"
#     specific_topic = "bone"

#     # Ensure the output folder exists
#     os.makedirs(output_folder, exist_ok=True)

#     # Cut the video based on silence and specific topic
#     cut_video_by_topic_and_silence(input_video_path, output_folder, specific_topic)











# from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.audio.io.AudioFileClip import AudioFileClip
# from pydub import AudioSegment
# import speech_recognition as sr
# import pytesseract
# from PIL import Image
# import os
# import re

# def extract_audio(video_path, audio_path):
#     video = VideoFileClip(video_path)
#     audio = video.audio
#     audio.write_audiofile(audio_path)

# def transcribe_audio(audio_path, default_transcript=""):
#     r = sr.Recognizer()

#     try:
#         audio = AudioSegment.from_file(audio_path)

#         with sr.AudioFile(audio_path) as source:
#             audio_data = r.record(source)

#         transcript = r.recognize_google(audio_data)
#         return transcript
#     except sr.UnknownValueError:
#         print("Speech Recognition could not understand audio")
#         return default_transcript
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         return default_transcript

# # ...

# def extract_text_from_video(video_path, start_time, end_time):
#     # Load video clip
#     video = VideoFileClip(video_path)

#     # Ensure end_time is not greater than the video duration
#     end_time = min(end_time, video.duration) if end_time is not None else video.duration

#     # Extract audio from the specified time range
#     audio_clip = AudioFileClip(video_path).subclip(start_time, end_time)
#     audio_path = "audio_temp.wav"
#     audio_clip.write_audiofile(audio_path, codec='pcm_s16le')

#     # Transcribe the audio with a default value in case of recognition failure
#     transcript = transcribe_audio(audio_path, default_transcript="No speech detected")
#     print("Transcript:", transcript)

#     # Extract text from video frames in the specified time range
#     video_clip = video.subclip(start_time, end_time)
#     text = ""

#     for frame in video_clip.iter_frames(fps=video.fps):
#         gray = Image.fromarray(frame).convert('L')
#         text += pytesseract.image_to_string(gray)

#     return text


# def find_silence_ranges(audio_path, silence_threshold=-40, silence_duration=1000):
#     audio = AudioSegment.from_file(audio_path)
#     silence_ranges = []

#     start_time = 0
#     current_range = None

#     for i, chunk in enumerate(audio[::silence_duration]):
#         if chunk.dBFS < silence_threshold:
#             if current_range is None:
#                 start_time = i * silence_duration
#                 current_range = [start_time, start_time + silence_duration]
#             else:
#                 current_range[1] = (i + 1) * silence_duration
#         elif current_range is not None:
#             silence_ranges.append(tuple(current_range))
#             current_range = None

#     if current_range is not None:
#         silence_ranges.append(tuple(current_range))

#     return silence_ranges

# def cut_video_by_topic_and_silence(video_path, output_folder, specific_topic, silence_threshold=-40, silence_duration=1000):
#     # Extract audio from the entire video
#     extract_audio(video_path, "audio_temp.wav")

#     # Find silence ranges in the audio
#     silence_ranges = find_silence_ranges("audio_temp.wav", silence_threshold, silence_duration)

#     # Cut video segments based on silence ranges and topic occurrence
#     for start_time, end_time in silence_ranges:
#         # Extract text from the silence period
#         text = extract_text_from_video(video_path, start_time / 1000, end_time / 1000)

#         # Check if the specific topic is present in the extracted text
#         if specific_topic.lower() in text.lower():
#             output_clip_path = os.path.join(output_folder, f"clip_{start_time}_{end_time}.mp4")

#             # Generate the short clip
#             video = VideoFileClip(video_path)
#             short_clip = video.subclip(start_time / 1000, end_time / 1000)
#             short_clip.write_videofile(output_clip_path, codec='libx264', audio_codec='aac')

#             print(f"Short clip generated successfully: {output_clip_path}")

# if __name__ == "__main__":
#     input_video_path = r"C:\Users\Zein\Desktop\New folder\t.mp4"
#     output_folder =  r"C:\Users\Zein\Desktop\New folder\test"
#     specific_topic = "bone"

#     # Ensure the output folder exists
#     os.makedirs(output_folder, exist_ok=True)

#     # Cut the video based on silence and specific topic
#     cut_video_by_topic_and_silence(input_video_path, output_folder, specific_topic)

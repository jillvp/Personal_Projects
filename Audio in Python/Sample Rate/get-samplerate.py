# Get Sample Rate: Specifically MP3 file

from mutagen.mp3 import MP3
audio_info = MP3('Rival_Consoles_-_Persona_-_9_Untravel.mp3').info

print(audio_info.sample_rate)

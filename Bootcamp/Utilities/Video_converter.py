import moviepy.editor as mp

clip = mp.VideoFileClip("music1.mp4").subclip(0,1500)
clip.audio.write_audiofile("Sleep Music - DNA Repairs.mp3")

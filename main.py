from pydub import AudioSegment

beat = AudioSegment.from_wav("beat.wav")

beat_low = beat.low_pass_filter(2000)
beat_low.export('low_pass.wav')

beat_fade = beat.fade_in(3000).fade_out(2000)
beat_fade.export('beat_fade.wav')

beat_left = beat_low.pan(-1) #method that aplly mono, -1 close to left speaker, 1 close to right speaker
beat_left.export('mono_left.wav')

beat_right = beat_low.pan(1) #method that aplly mono, -1 close to left speaker, 1 close to right speaker
beat_right.export('mono_right.wav')

beat_final = beat_low * 2 + beat_fade + beat_left + beat_right + beat_left + beat_right + beat_low 
beat_final.export('final_song.wav')
 
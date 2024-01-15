'''
import vlc
Instance = vlc.Instance("prefer-insecure")
player = Instance.media_player_new()
Media = Instance.media_new('https://www.youtube.com/watch?v=vG2PNdI8axo')

Media.get_mrl()
player.set_media(Media)
player.play()
while str(player.get_state()) != "State.Ended":
    pass
player.stop()
'''
import vlc

inst  = vlc.Instance()
param=[
    "https://www.youtube.com/watch?v=vG2PNdI8axo"
    ,"sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=http{mux=ffmpeg{mux=flv},dst=:8080/}"
    ]
Media = inst.media_new("https://www.youtube.com/watch?v=vG2PNdI8axo")
player = Media.player_new_from_media()
player.play()

while str(player.get_state()) != "State.Ended":
    pass
player.stop()

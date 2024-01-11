import vlc
'''
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new("https://www.youtube.com/watch?v=vG2PNdI8axo")
Media.get_mrl()
player.set_media(Media)
player.play()
'''
import os

#os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"] 
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

os.add_dll_directory(os.getcwd())
import mpv
player = mpv.MPV(ytdl=False)

player.play('https://www.youtube.com/watch?v=vG2PNdI8axo')
#player.wait_for_playback()
player.communicate()
import vlc
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('https://www.youtube.com/watch?v=vG2PNdI8axo')
Media.get_mrl()
player.set_media(Media)
player.play()
            

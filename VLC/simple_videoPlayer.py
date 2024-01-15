import vlc 
  
# importing pafy module 
import yt_dlp as youtube_dl
import pafy 

# url of the video 
url = "https://www.youtube.com/watch?v=vG2PNdI8axo"
#url = "vG2PNdI8axo"
#video = pafy.new(url) 
#best = video.getbest() 

# creating vlc media player object 
#media = vlc.MediaPlayer(best.url)
media = vlc.MediaPlayer(url) 
  
# start playing video 
media.play() 

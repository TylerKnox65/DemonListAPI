from pathlib import Path

import vlc
import PySimpleGUI as sg

Instance = vlc.Instance()
player = Instance.media_player_new()

sg.theme("DarkBlue")

layout = [
    [sg.Input(key='-IN-', visible=False, enable_events=True),
     sg.FileBrowse(file_types=(("MP4 Files", "*.mp4"),))],
    [sg.Graph((640, 480), (0, 0), (640, 480), key='-CANVAS-')],     # OK if use [sg.Canvas(size=(640, 480), key='-CANVAS-')],
        
]
window = sg.Window('Title', layout, finalize=True)

video_panel = window['-CANVAS-'].Widget.master
# set the window id where to render VLC's video output
h = video_panel.winfo_id()  # .winfo_visualid()?
player.set_hwnd(h)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-IN-':
        video = values[event]
        
        
        if Path(video).is_file():
            m = Instance.media_new(str(video))  # Path, unicode
            player.set_media(m)
            player.play()
        
player.stop()
window.close()
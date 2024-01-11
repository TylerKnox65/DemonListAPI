#!python3

from typing import Any
import PySimpleGUI as sg
import requests
import json
from PIL import Image
import io
import cloudscraper
import loadingscreen

class main():
    def __init__(self) -> None:
        #Import Modules
        #Using request we access: https://pointercrate.com/api/v1/demons
        self.window_size = (600,800)
        self.num = 1
        self.loadedto100 = False
        self.loadedpast100 = False
        self.openwindow()
        self.request()
    
        
    def request(self,searchparams=None):
        #sg.one_line_progress_meter("Loading",1,1000,key="real") #Literally the worst loading window
        if searchparams != None: 
            self.req = requests.get(searchparams)
            self.data = json.loads(self.req.text)
        
        else:
            self.req = requests.get('https://pointercrate.com/api/v2/demons/listed/?limit=75')
            self.data = json.loads(self.req.text)
        #sg.one_line_progress_meter_cancel(key="real")
        return self.data
    def openwindow(self):
        #sg.theme('DarkAmber')
        sg.change_look_and_feel("Topanga")
        mainList = self.request()
        col_layout = [[sg.Text("Top 75",font=("Helvetica", 11))]]
        self.num = 1
        for i in mainList:
            thumbnail = self.convertimage(i['thumbnail'])
            #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
            col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}"),sg.T("|"),sg.T(f"Verifier: {i['verifier']['name']}")])
            col_layout.append([sg.Image(data=thumbnail)])
            col_layout.append([sg.T("")]) #Padding
        self.num = 0
        print(mainList)
        #col_layout.append()
        Column = sg.Column(col_layout,vertical_scroll_only=True,scrollable=True,size=(self.window_size[0],self.window_size[1]-50),sbar_width=5,sbar_background_color="grey",sbar_trough_color="black",key="col_key",size_subsample_height=99999)
        layout = [[Column],[sg.Button("Load more?",key="load")]]
        self.window = sg.Window('DemonList', layout,element_justification="r",finalize=True,keep_on_top=False,grab_anywhere=True,size=self.window_size,resizable=True)
        self.window['col_key'].Widget.configure(borderwidth=1, relief=sg.DEFAULT_FRAME_RELIEF)
        self.mainLoop()
    def mainLoop(self,temp = None):
         while True:             
            window, event, values = sg.read_all_windows()
            if event == None:
                raise SystemExit
            else:
                pass
                #Issue caused possibly by running out of memory.
                '''
                if event in "load":
                    if self.loadedto100:
                        if not self.loadedpast100:
                            loaded = self.request(searchparams="https://pointercrate.com/api/v2/demons/listed/?after=100")
                            col_layout = [[]]
                           
                            for i in loaded:
                                col_layout = [[]]
                                thumbnail = self.convertimage(i['thumbnail'])
                                #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
                                col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}")])
                                col_layout.append([sg.Image(data=thumbnail)])
                                col_layout.append([sg.Text("")]) #Padding
                                self.window.extend_layout(self.window["col_key"], col_layout)
                                self.window['col_key'].contents_changed()
                                self.window.refresh()
                                self.window["col_key"].Widget.canvas.config(scrollregion=window['col_key'].Widget.canvas.bbox('all'))
                                
                            print(loaded)
                            #self.window.extend_layout(self.window["col_key"], col_layout)
                            self.loadedpast100 = True
                        else:
                            pass
                    else:
                        loaded = self.request(searchparams="https://pointercrate.com/api/v2/demons/listed/?after=50")
                        col_layout = [[]]
                        for i in loaded:
                            col_layout = [[]]
                            thumbnail = self.convertimage(i['thumbnail'])
                            #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
                            col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}"),sg.T("|")])
                            col_layout.append([sg.Image(data=thumbnail)])
                            col_layout.append([sg.T("")]) #Padding
                            self.window.extend_layout(self.window["col_key"], col_layout)
                            self.window['col_key'].contents_changed()
                            self.window.refresh()
                            self.window["col_key"].Widget.canvas.config(scrollregion=window['col_key'].Widget.canvas.bbox('all'))
                            
                            
                        print(loaded)
                        #Code that updates the size of the column to hopefully include more options. Doesn't work?
                        #options = {'width':self.window_size[0], 'height':self.window_size[1] * 2}
                        #self.window['col_key'].Widget.canvas.configure(**options)
                        #self.window.extend_layout(self.window["col_key"], col_layout)
                        self.loadedto100 = True
                    self.window['col_key'].contents_changed()
                    self.window.refresh()
                    self.window["col_key"].Widget.canvas.config(scrollregion=window['col_key'].Widget.canvas.bbox('all'))
                    '''
    def convertimage(self,url):
        #sg.one_line_progress_meter("Loading",self.num,50,key="real") #Literally the worst loading window...AGAIN, being replaced by loadingscreen.py when i finish
        if self.num >= 75:
            loadingscreen.main().close()

        else:
            loadingscreen.main().popup(self.num)
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            )
            .get(url)
            .content
        )

        pil_image = Image.open(io.BytesIO(jpg_data))
        cur_width, cur_height = pil_image.size
        scale = (self.window_size[0] / cur_width) - 0.25
        pil_image = pil_image.resize((int(cur_width*scale), int(cur_height*scale)))
        png_bio = io.BytesIO()
        pil_image.save(png_bio, format="PNG")
        png_data = png_bio.getvalue()
        self.num += 1
        #sg.one_line_progress_meter_cancel(key="real")

        return png_data
main()
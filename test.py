import PySimpleGUI as sg
import requests
import json
from PIL import Image
import io
import cloudscraper
req = requests.get('https://pointercrate.com/api/v2/demons/listed/?limit=50')
data = json.loads(req.text)
print(data)
req = requests.get('https://pointercrate.com/api/v2/demons/listed/?after=50')
data = json.loads(req.text)
print(data)

class main():
                    def __init__(self) -> None:
                            sg.change_look_and_feel("Topanga")
                            self.window_size = (600,800)
                            col_layout = [[sg.T("Top 50"),sg.Button("Press",key="press")]]
                            Column = sg.Column(col_layout,vertical_scroll_only=True,scrollable=True,size=(self.window_size[0],self.window_size[1]-50),sbar_width=5,sbar_background_color="grey",sbar_trough_color="black",key="col_key")
                            layout = [[Column],[sg.Button("Load more?",key="load")]]
                            self.window = sg.Window('DemonList', layout,element_justification="r",finalize=True,keep_on_top=True,grab_anywhere=True,size=self.window_size,resizable=True)
                            
                            self.testfunc()
                    def mainLoop(self):
                        loaded = self.request(searchparams="https://pointercrate.com/api/v2/demons/listed/?after=50")
                        col_layout = [[]]
                        for i in loaded:
                            thumbnail = self.convertimage(i['thumbnail'])
                            #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
                            col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}")])
                            col_layout.append([sg.Image(data=thumbnail)])
                            col_layout.append([sg.T("")]) #Padding
                        print(loaded)
                        #Code that updates the size of the column to hopefully include more options. Doesn't work?
                        #options = {'width':self.window_size[0], 'height':self.window_size[1] * 2}
                        #self.window['col_key'].Widget.canvas.configure(**options)
                        self.window.extend_layout(self.window["col_key"], col_layout)
                        self.loadedto100 = True
                        self.window['col_key'].contents_changed()
                        self.window.refresh()
                        self.window["col_key"].Widget.canvas.config(scrollregion=window['col_key'].Widget.canvas.bbox('all'))
                    def testfunc(self):
                            while True:             
                                window, event, values = sg.read_all_windows()
                                if event == None:
                                    raise SystemExit
                                elif event in "press":
                                       self.mainLoop()
                    def convertimage(self,url):
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
                       

                        return png_data
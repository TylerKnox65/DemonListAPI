import PySimpleGUI as sg
from PIL import Image
import io
import cloudscraper
import json
import requests
import webbrowser
class main():
    def __init__(self) -> None:
        pass
    def layout(self,mainList,searchparam):
        self.mainList = mainList
        self.window_size = (600,500)
        self.found = False
        col_layout = []
        print(type(mainList))
        print(searchparam)
        for i in mainList:
            #print(i,searchparam)
            try:
                #print(i.values())
                #if any(any(searchparam in s for s in subList) for subList in i.values()): Any return a false answer
                
                for k in i.values():
                    print(k)
                    if searchparam in str(k):
                        print(i.values())
                        self.found = True
                        print("FOUND\n\n\n")
                        print(i,i["thumbnail"],i['name'])
                        thumbnail = self.convertimage(i['thumbnail'])
                        #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
                        col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}"),sg.T("|"),sg.T(f"Verifier: {i['verifier']['name']}")])
                        col_layout.append([sg.Image(data=thumbnail)])
                        #play=self.convertimage("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngall.com%2Fwp-content%2Fuploads%2F5%2FPlay-Button-PNG-Picture.png&f=1&nofb=1&ipt=3ae1060bc1ec91c7474f0e20bca3a5eba32cba38a62491e20ad7c1c5ba88771f&ipo=images")
                        col_layout.append([sg.Button("Play Video!",key=i['video'])])
                        col_layout.append([sg.HorizontalSeparator(color='black')]) #Padding
                        break
                        
                    else:
                        pass
                '''
                if self.found:
                    print("FOUND\n\n\n")
                    print(i,i["thumbnail"],i['name'])
                    thumbnail = self.convertimage(i['thumbnail'])
                    #col_layout.append([[sg.T(i['name']),sg.T(f"ID:{i['id']}")],[sg.Image(data=thumbnail)]]) <- Unused for being hard to read + wrong layout.
                    col_layout.append([sg.T(i['name']),sg.T("|"),sg.T(f"ID: {i['id']}"),sg.T("|"),sg.T(f"Placement: {i['position']}"),sg.T("|"),sg.T(f"Verifier: {i['verifier']['name']}")])
                    col_layout.append([sg.Image(data=thumbnail)])
                    #play=self.convertimage("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngall.com%2Fwp-content%2Fuploads%2F5%2FPlay-Button-PNG-Picture.png&f=1&nofb=1&ipt=3ae1060bc1ec91c7474f0e20bca3a5eba32cba38a62491e20ad7c1c5ba88771f&ipo=images")
                    col_layout.append([sg.Button("Play Video!",key=i['video'])])
                    col_layout.append([sg.HorizontalSeparator(color='black')]) #Padding
                '''
            except Exception as e:
                print(e)
        Column = sg.Column(col_layout,vertical_scroll_only=True,scrollable=True,size=(self.window_size[0],self.window_size[1]-50),sbar_width=5,sbar_background_color="grey",sbar_trough_color="black",key="col_key",size_subsample_height=99999)
        layout = [[Column],[]]
        self.window = sg.Window('DemonList', layout,element_justification="r",finalize=True,keep_on_top=False,grab_anywhere=True,size=self.window_size,resizable=True)

        #self.mainLoop()
    def mainLoop(self):
       while True: 
            window, event, values = sg.read_all_windows()
            print(event)
            for i in self.mainList:
                    if event == i['video']:
                        webbrowser.open(event, new=2)
            if event == None:
                print(window)
                window.close()
    def convertimage(self,url):
        #sg.one_line_progress_meter("Loading",self.num,50,key="real") #The worst loading window..., being replaced by loadingscreen.py when I finish
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            )
            .get(url)
            .content
        )

        pil_image = Image.open(io.BytesIO(jpg_data))
        cur_width, cur_height = pil_image.size
        scale = (600 / cur_width) - 0.25
        pil_image = pil_image.resize((int(cur_width*scale), int(cur_height*scale)))
        png_bio = io.BytesIO()
        pil_image.save(png_bio, format="PNG")
        png_data = png_bio.getvalue()
     
      

        return png_data
    

if __name__ == "__main__":
    req = requests.get('https://pointercrate.com/api/v2/demons/listed/?limit=75')
    data = json.loads(req.text)
    main().layout(mainList=data,searchparam="A")
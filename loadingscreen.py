import PySimpleGUI as sg
import time

class main():
    def __init__(self) -> None:
        sg.change_look_and_feel("Topanga")
        #BAR_MAX = 75
        #layout = [[sg.Text('Progress')],
          #[sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')]]
        #self.window = sg.Window('Loading!', layout,element_justification="r",finalize=True,keep_on_top=False,grab_anywhere=True,size=(250,75),resizable=True)
        #self.mainLoop()
    def close(self):
            sg.one_line_progress_meter_cancel(key="real")
            
    def popup(self,i):
            sg.one_line_progress_meter("Loading",i,75,key="real")
    def mainLoop(self):
       i = 0
       while True:
            i+=1             
            window, event, values = sg.read_all_windows()
            self.window['-PROG-'].update(i+1)
            if event == None:
                raise SystemExit
            else:
                pass
if __name__ == "__main__":
    main()
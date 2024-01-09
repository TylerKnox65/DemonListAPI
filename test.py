import PySimpleGUI as sg
import requests
import json
req = requests.get('https://pointercrate.com/api/v2/demons/listed/?limit=50')
data = json.loads(req.text)
print(data)
req = requests.get('https://pointercrate.com/api/v2/demons/listed/?after=50')
data = json.loads(req.text)
print(data)
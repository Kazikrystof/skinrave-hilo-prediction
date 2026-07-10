import pytesseract
import cv2
import numpy as np
from mss import mss
import time, os
import json
import pyautogui
import keyboard
import subprocess
import random

#test

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

subprocess.Popen([
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--incognito",
    "https://skinrave.gg/en/hilo"
])

time.sleep(2)

region = {
    "left": -945,
    "top": 324,
    "width": 60,
    "height": 56
}

           
def card_value(text):
        values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}
        return values[text]

with open("stats.json", "r") as file:
                data = json.load(file)
test = False
with mss() as sct:
    hilow = [0,0]
    previous_card = None
    previous_value = None  

    while test == False:
        time_randomizer = random.uniform(0.01, 0.1)
        pyautogui.click(-847,260)
        time.sleep(0.4 + time_randomizer)
        sct_img = sct.grab(region)
        frame = np.array(sct_img)
        text = pytesseract.image_to_string(frame, lang="eng", config="--psm 6")
        text = text.strip()

        
        if text in data:

            card = text
            value = card_value(card)

            data[card]["stats"]["count"] += 1
            data["total_records"] += 1

            if previous_card is not None:

                if value > previous_value:
                    data[previous_card]["stats"]["next_higher"] += 1

                elif value < previous_value:
                    data[previous_card]["stats"]["next_lower"] += 1

                else:
                    data[previous_card]["stats"]["equal"] += 1

            previous_card = card
            previous_value = value

            with open("stats.json", "w") as file:
                json.dump(data, file, indent=4)
                    
            if keyboard.is_pressed("right shift"):
                        test = True
            print(text)
            
time.sleep(1)
os.system("cls")       


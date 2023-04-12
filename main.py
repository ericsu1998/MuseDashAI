import easyocr
import pyautogui
import pydirectinput
import subprocess
import time

def screenshot(file):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(file) 

def openGame():
    subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 774171")
    time.sleep(15)
    pydirectinput.press('enter', presses=2, interval=5) 

def closeGame():
    pydirectinput.press('esc', presses=2, interval=5)
    pydirectinput.press('enter')

def getCurrentSong():
    f = 'currentSong.png'
    screenshot(f)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(f, detail = 0)
    return result[2]

def startGame():
    #Assumes you're in song selection menu
    pydirectinput.press('enter')
    currentSong = getCurrentSong()
    pydirectinput.press('enter')
    return currentSong

def playGameWithDumbAi():
    time.sleep(5)
    startTime = time.time()
    pydirectinput.PAUSE = 0.01
    while(time.time() - startTime < 180):
        pydirectinput.press('d')
        pydirectinput.press('j')

def endGame():
    pydirectinput.press('enter')
    time.sleep(5)

def main():
    openGame()
    currentSong = startGame()
    playGameWithDumbAi()
    screenshot(f'{currentSong}_dumbAI.png')
    endGame()
    closeGame()

if __name__ == "__main__":
    main()





import pyautogui as pyg
from time import sleep


pyg.press('win')
pyg.write('edge')
pyg.press('enter')
sleep(2)
pyg.write(r'https://apps.powerapps.com/play/66bfb990-d494-4e5b-a347-91c337719c6d')
pyg.press('enter')
pyg.press('f11')
sleep(6)
pyg.click(x=800, y=652)
sleep(5)
pyg.hotkey('alt', 'f4')



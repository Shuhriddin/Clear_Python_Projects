import webbrowser
from urllib.parse import quote
import pyautogui
import time

# phone_number_list = ["+998991259009", "+998991176060"]
with open('phones.txt', 'r', encoding='utf-8') as phones_file:
    phones_and_names_list = phones_file.readlines()

# print(phones_and_names_list)
screen_width, screen_height = pyautogui.size()

for row in phones_and_names_list:
    row_list = row.split(',')
    phone = row_list[0].strip()
    name = row_list[1].strip()

    message = f"Здравствуйте {name} У нас началась распродажа! Скидка до -30%!"
    encoded_message = quote(message.encode('utf-8'))
    webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}&text={encoded_message}')
    time.sleep(15)


    pyautogui.click(screen_width/2, screen_height/2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('control', 'w')

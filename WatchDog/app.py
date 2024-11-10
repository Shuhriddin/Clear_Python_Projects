import pyautogui

# Перемешаем мышь на кооординаты (100, 200)
pyautogui.moveTo(100, 200, duration=1)

# Делаем клик по текущую позиции мыши
pyautogui.click()

# Вводим текст
pyautogui.write('Hello, world!')
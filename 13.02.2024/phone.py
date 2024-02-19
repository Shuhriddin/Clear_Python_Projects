import csv
import tkinter as tk
from tkinter import filedialog


PHONE_DICT = {}
def add_contact():
    try:
        user_surname_name = input("\nВведите фамилия и имя через пробел: ").title()
        surname, name = user_surname_name.split()
        if (surname, name) in PHONE_DICT:
            print("Такого абонент есть в списке")
        else:
            user_phone_number = int(input("Введите телефон номер абонента: "))
            PHONE_DICT[surname, name] = user_phone_number
            print("В списке существует: {}".format(PHONE_DICT))
            print("АБОНЕНТ УСПЕШНО ДОБАВЛЕНО!!!")
    except ValueError as value:
        print("ОШИБИБКА!!! Введите (фамилия и имя) в правильном порядке... {}".format(value))
    return PHONE_DICT

def search_contact():
    user_search_name = input("Введите фамилия или имя поисковаемого абонента: ").title()
    is_Prime = False
    try:
        for key_search, value_search in PHONE_DICT.items():
            if user_search_name in key_search:
                print("*****", " ".join(key_search), "|", value_search, "*****")
                is_Prime = True
        if not is_Prime:
            print("Такого абонента нету в списке!!!")
    except Exception as file_error:
        print("ОШИБКА!!! Введите поисковаемого абонента в правильном порядке... {}".format(file_error))
    return PHONE_DICT

def del_contact():
    try:
        user_delete = input("Введите удаляемого абонента: ").title()
        user_del_surname, user_del_name = user_delete.split()
        if (user_del_surname, user_del_name) in PHONE_DICT:
            del PHONE_DICT[user_del_surname, user_del_name]
            print("{} УСПЕШНО УДАЛЕНО!!!".format(user_delete))
            print("В списке существует: {}".format(PHONE_DICT))
        else:
            print("Абонент не найден!!!")
    except Exception as del_phone:
        print("ОШИБКА!!! Введите в правильном порядке => {}".format(del_phone))
    return PHONE_DICT

def download_file():
    folder = filedialog.askdirectory() # qaysi papkaga saqlashni so`rash uchun => tkinter-filedialog
    if folder:
        with open(folder + "/phone.txt", "w", encoding="UTF-8") as write_file:
            for key, value in PHONE_DICT.items():
                write_file.write(str(key) + " - тел.номер: " + str(value) + "\n")

        with open(folder + "/phone.csv", "w", encoding="UTF-8", newline='') as write_file:
            writer = csv.writer(write_file)
            for key, value in PHONE_DICT.items():
                writer.writerow([key[0], key[1], value])
        print("Файлы успешно сохранены.")
    else:
        print("Неверное место сохранения.")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Выберите папка: {folder}")
    return folder

if __name__ == '__main__':
    while True:
        print()
        print("1.Добавить контакт\n2.Найти контакт\n3.Удалить \n4.Завершить работу")
        action = input("Введите действия: ")
        if action == "1":
            add_contact()
        elif action == "2":
            search_contact()
        elif action == "3":1
        11
            del_contact()
        elif action == "4":
            break

    root = tk.Tk()
    root.withdraw()
    save_dir = open_file_dialog()

    if save_dir:
        print("Скачивается...")
        download_file()
    else:
        print("Неверное место сохранения.")

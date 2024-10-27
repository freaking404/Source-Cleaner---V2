import os
import time
import customtkinter
from customtkinter import *
from PIL import Image
from pynput.keyboard import Key, Controller

Keyboard = Controller()


def press(key):
    Keyboard.press(key)
    Keyboard.release(key)


def t(num):
    time.sleep(num)


def temp_clean():
    directory_temp_1 = ('C:\\Windows\\Temp')
    directory_temp_2 = ('C:\\Users\\YOUR USER NAME\\AppData\\Local\\Temp')

    for filename in os.listdir(directory_temp_1):
        file_path = os.path.join(directory_temp_1, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'File elimination failed: {file_path}. Exception: {e}')

    t(2)

    for filename in os.listdir(directory_temp_2):
        file_path = os.path.join(directory_temp_2, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'File elimination failed: {file_path}. Exception: {e}')


def prefetch_clean():
    directory_prefetch = ('C:\\Windows\\Prefetch')

    for filename in os.listdir(directory_prefetch):
        file_path = os.path.join(directory_prefetch, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'File elimination failed: {file_path}. Exception: {e}')


def download_clean():
    directory_download = ('C:\\Windows\\SoftwareDistribution\\Download')

    for filename in os.listdir(directory_download):
        file_path = os.path.join(directory_download, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f'File elimination failed: {file_path}. Exception: {e}')


def disk_clean():
    press(Key.cmd)
    t(1.5)
    Keyboard.type('Disk Clean-up')
    t(1.5)
    press(Key.enter)


def start_popup_destroy():
    popup_label_1.destroy()


cleaner_app = CTk()

cleaner_app.title('sᴏᴜʀᴄᴇ ᴄʟᴇᴀɴᴇʀ')
cleaner_app.resizable(False, False)
cleaner_app.geometry('800x500')
cleaner_app.iconbitmap('E:\\files\\code\\data\\cleaner.ico')
cleaner_app._set_appearance_mode('system')
set_default_color_theme('E:\\files\\code\\data\\aqua.json')

cleaner_background = customtkinter.CTkImage(light_image=Image.open('E:\\files\\code\\data\\cleaner_wbg.jpg'),
                                       dark_image=Image.open('E:\\files\\code\\data\\cleaner_bbg.jpg'),
                                       size=(424, 500))
cleaner_label_1 = customtkinter.CTkLabel(master=cleaner_app,
                              text='',
                              image=cleaner_background)
cleaner_label_1.pack()
cleaner_label_1.place(x=0, y=0)
cleaner_frame = customtkinter.CTkFrame(master=cleaner_app,
                              width=300,
                              height=400,
                              corner_radius=15)
cleaner_frame.pack()
cleaner_frame.place(x=462, y=52)
cleaner_button_1 = customtkinter.CTkButton(master=cleaner_frame,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ',
                                  command=download_clean)
cleaner_button_1.pack()
cleaner_button_1.place(relx=0.175, rely=0.15)
cleaner_button_2 = customtkinter.CTkButton(master=cleaner_frame,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴛᴇᴍᴘ',
                                  command=temp_clean)
cleaner_button_2.pack()
cleaner_button_2.place(relx=0.175, rely=0.35)
cleaner_button_3 = customtkinter.CTkButton(master=cleaner_frame,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴘʀᴇғᴇᴛᴄʜ',
                                  command=prefetch_clean)
cleaner_button_3.pack()
cleaner_button_3.place(relx=0.175, rely=0.55)
cleaner_button_4 = customtkinter.CTkButton(master=cleaner_frame,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴅɪsᴋ',
                                  command=disk_clean)
cleaner_button_4.pack()
cleaner_button_4.place(relx=0.175, rely=0.75)

var_1 = StringVar(value='true')


def theme_changer():
    if var_1.get() == 'false':
        set_appearance_mode('light')
    elif var_1.get() == 'true':
        set_appearance_mode('dark')


cleaner_switch = customtkinter.CTkSwitch(master= cleaner_app,
                                      text='ᴛʜᴇᴍᴇ',
                                      command=theme_changer,
                                      button_length=6,
                                      variable=var_1, offvalue='false', onvalue='true')
cleaner_switch.pack()
cleaner_switch.place(x=560, y=460)

popup_background = customtkinter.CTkImage(light_image=Image.open('E:\\files\\code\\data\\cleaner_wpat.jpg'),
                                       dark_image=Image.open('E:\\files\\code\\data\\cleaner_bpat.jpg'),
                                       size=(800, 500))
popup_label_1 = customtkinter.CTkLabel(master=cleaner_app,
                                     text='',
                                     image=popup_background)
popup_label_1.pack()
popup_label_1.place(x=0, y=0)
popup_frame = customtkinter.CTkFrame(master=popup_label_1,
                              width=220,
                              height=120)
popup_frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
popup_label_2 = customtkinter.CTkLabel(master=popup_frame,
                              text='ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ᴄʟᴇᴀɴᴇʀ!\nᴛʜɪs ᴄʟᴇᴀɴᴇʀ ɪs ᴏᴘᴇɴ sᴏᴜʀᴄᴇ!',
                              justify=CENTER)
popup_label_2.pack()
popup_label_2.place(relx=0.49, rely=0.4, anchor=customtkinter.CENTER)
popup_button = customtkinter.CTkButton(master=popup_frame,
                                       text='ᴏᴋ',
                                       hover_color='grey',
                                       fg_color='black',
                                       command=start_popup_destroy,
                                       width=220,
                                       height=30)
popup_button.pack_slaves()
popup_button.place(relx=0, rely=0.775)

cleaner_app.mainloop()

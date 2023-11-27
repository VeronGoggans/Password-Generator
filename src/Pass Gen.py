import random
import customtkinter
from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
from theme import Theme
from _keyboard import Keyboard
import os 


class PasswordGenerator:
    def __init__(self):

        self.no_value_message = 'Move slider to set password length.'
        self.password_length = 0
        self.password = []
        self.characters: list = Keyboard.characters()
        self.symbols: list = Keyboard.symbols()
        self.numbers: list = Keyboard.numbers()
        self.keys: list = self.characters + self.symbols + self.numbers
        self.cwd: str = os.getcwd()

        # Customtkinter window settings.
        self.window = CTk()
        customtkinter.set_appearance_mode('dark')

        self.window.title('Pass Gen')
        self.window.geometry('600x500') 
        self.window.minsize(600, 500)
        self.window.maxsize(600, 500)
        self.light_img = f'{self.cwd}/Password-Generator/img/light/app_image_lightmode.png'
        self.dark_img = f'{self.cwd}/Password-Generator/img/dark/app_image_darkmode.png'
        self.app_icon = PhotoImage(file=f'{self.cwd}/Password-Generator/img/app_icon2.png')
        self.window.iconphoto(False, self.app_icon)

        self.theme = Theme()

        # App colors.
        self.primary = ''
        self.secondary = ''
        self.tertiary = ''
        self.charcoal = ''
        self.neon_purple = ''
        self.text = ''
        self.__set_colors()


        # Customtkinter widgets below.
        self.background_frame = CTkFrame(self.window, fg_color=self.primary, corner_radius=0) 
        self.ctk_app_image = CTkImage(dark_image=Image.open(f'{self.__set_image()}'), size=(150, 150)) 


        self.app_image_label = CTkLabel(self.background_frame, text='', image=self.ctk_app_image)   
        self.password_length_label = CTkLabel(self.background_frame, text='Password length: 0', font=('Helvetica', 15), text_color=self.text) 
        self.password_label = CTkLabel(self.background_frame, text='Generated password', font=('Helvetica', 15), text_color=self.text)

        self.password_length_entry = CTkEntry(self.background_frame, width=40, fg_color=self.primary, border_color=self.secondary, border_width=2)
        self.password_entry = CTkEntry(self.background_frame, justify='center' , width=300, fg_color=self.primary, border_color=self.secondary, text_color=self.text, border_width=2) 

        self.gen_password_button = CTkButton(self.background_frame, text='Generate', font=('Helvetica', 20), fg_color=self.secondary, hover_color=self.tertiary, text_color='#ffffff', width=300, height=40, corner_radius=20, command=self.__run)
        self.password_length_slider = CTkSlider(self.background_frame, width=300, from_=0, to=35, fg_color=self.tertiary, button_color=self.charcoal, button_hover_color=self.charcoal, progress_color=self.neon_purple, command=self.__sliding)

        # Key bindings.
        self.window.bind('<Left>', lambda event: self.__left_arrow(self.password_length_slider.get()))
        self.window.bind('<Right>', lambda event: self.__right_arrow(self.password_length_slider.get()))
        self.window.bind('<Control-m>', lambda event: self.__switch_theme())
        
        # Calling the render method will place all CTK widgets on the window.
        self.__render()
        self.__center_entry_value(self.no_value_message) 
        self.window.mainloop()

    
    def __render(self):
        self.background_frame.pack(fill='both', expand=True)
        self.app_image_label.pack(side=TOP, pady=30)
        self.password_length_label.place(x=235, y=220)
        self.password_label.place(x=230, y=290)
        self.password_entry.place(x=150, y=325)
        self.gen_password_button.place(x=150, y=400)
        self.password_length_slider.place(x=150, y=250)
        self.password_length_slider.set(0)


    def __run(self):
        self.__user_input()
        self.__center_entry_value(self.__generate())
        self.__readonly()


    def __user_input(self):
        self.password_length = int(round(self.password_length_slider.get()))

    
    def __generate(self):
        self.__editable()
        self.__clear_old_password()

        if self.__no_value_check():
            return self.no_value_message
        
        for _ in range(self.password_length):
            self.password.append(random.choice(self.keys))

        random.shuffle(self.password)
        return ''.join(self.password)
    

    def __no_value_check(self):
        return self.password_length == 0

    def __readonly(self):
        self.password_entry.configure(state='readonly')

    def __editable(self):
        self.password_entry.configure(state='normal')

    def __clear_old_password(self):
        self.password_entry.delete(0, END)
        self.password.clear()

    def __center_entry_value(self, str_value: str):
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, str_value)

    def __sliding(self, value):
        self.password_length_label.configure(text=f'Password length {round(value)}')

    def __left_arrow(self, value):
        if value > 0:
            value -= 1
            self.password_length_slider.set(round(value))
            self.__sliding(value)

    def __right_arrow(self, value):
        if value < 35:
            value += 1
            self.password_length_slider.set(round(value))
            self.__sliding(value)

    def __set_colors(self):
        theme_colors = self.theme.colors()
        self.primary = theme_colors[0]
        self.secondary = theme_colors[1]
        self.tertiary = theme_colors[2]
        self.charcoal = theme_colors[3]
        self.neon_purple = theme_colors[4]
        self.text = theme_colors[5]
        # customtkinter.set_appearance_mode(current_theme)

    def __get_colors(self):
        return self.theme.colors()

    def __set_image(self):
        theme = self.theme.get_theme()
        if theme == 'light':
            return self.light_img
        if theme == 'dark':
            return self.dark_img
        
    def __switch_image(self):
        self.ctk_app_image.configure(dark_image=Image.open(f'{self.__set_image()}'), size=(150, 150))
        
    def __switch_theme(self):
        self.theme.set_theme()
        self.__set_colors()
        theme_colors = self.__get_colors()
        self.background_frame.configure(fg_color=theme_colors[0])
        self.password_entry.configure(fg_color=theme_colors[0], text_color=theme_colors[-1])
        self.password_label.configure(text_color=theme_colors[-1])
        self.password_length_label.configure(text_color=theme_colors[-1])
        self.__switch_image()


my_password_generator = PasswordGenerator()
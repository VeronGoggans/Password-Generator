import os  
from configparser import ConfigParser

class Theme:
    def __init__(self) -> None:
        self.parser = ConfigParser()
        self.settings_file = f'{os.getcwd()}/Password-Generator/src/settings.ini'


    def colors(self) -> list: 
        theme = self.get_theme()
        self.parser.read(self.settings_file)
        primary = self.parser.get(theme, 'primary')
        secondary = self.parser.get(theme, 'secondary')
        tertiary = self.parser.get(theme, 'tertiary')
        slider_button = self.parser.get(theme, 'slider_button')
        accent = self.parser.get(theme, 'accent')
        text = self.parser.get(theme, 'text')
        return [primary, secondary, tertiary, slider_button, accent, text]
    

    def get_theme(self):
        self.parser.read(self.settings_file)
        return self.parser.get('theme', 'theme')
    

    def set_theme(self):
        self.parser.read(self.settings_file)

        if len(self.get_theme()) == 4:
            self.parser.set('theme', 'theme', 'light')
        else:
            self.parser.set('theme', 'theme', 'dark')

        with open(self.settings_file, 'w') as configfile:
            self.parser.write(configfile)

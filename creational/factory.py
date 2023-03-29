from abc import ABC, abstractmethod


class Dialog(ABC):
    @staticmethod
    @abstractmethod
    def create_button():
        pass


class Button(ABC):
    def __init__(self):
        self.is_rendered = False
        
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def on_click(self):
        pass


class WindowsButton(Button):
    def render(self):
        if not self.is_rendered:
            print("Rendering Windows Button!")
            self.is_rendered = True
        else:
            print("Button already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("Windows Button Action")


class HTMLButton(Button):
    def render(self):
        if not self.is_rendered:
            print("Rendering HTML Button!")
            self.is_rendered = True
        else:
            print("Button already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("HTML Button Action")


class WindowsDialog(Dialog):
    @staticmethod
    def create_button():
        return WindowsButton()


class WebDialog(Dialog):
    @staticmethod
    def create_button():
        return HTMLButton()


button1 = WindowsDialog.create_button()
button1.render()
button1.on_click()

button2 = WebDialog.create_button()
button2.render()
button2.on_click()


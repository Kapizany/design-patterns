from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_button():
        pass
    
    @staticmethod
    @abstractmethod
    def create_checkbox():
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


class CheckBox(ABC):
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


class MACButton(Button):
    def render(self):
        if not self.is_rendered:
            print("Rendering MAC Button!")
            self.is_rendered = True
        else:
            print("Button already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("MAC Button Action")


class WindowsCheckBox(CheckBox):
    def render(self):
        if not self.is_rendered:
            print("Rendering Windows CheckBox!")
            self.is_rendered = True
        else:
            print("CheckBox already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("Windows CheckBox Action")


class HTMLCheckBox(CheckBox):
    def render(self):
        if not self.is_rendered:
            print("Rendering HTML CheckBox!")
            self.is_rendered = True
        else:
            print("CheckBox already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("HTML CheckBox Action")


class MACCheckBox(CheckBox):
    def render(self):
        if not self.is_rendered:
            print("Rendering MAC CheckBox!")
            self.is_rendered = True
        else:
            print("CheckBox already rendered!")
    
    def on_click(self):
        if self.is_rendered:
            print("MAC CheckBox Action")


class WindowsFactory(GUIFactory):
    @staticmethod
    def create_button():
        return WindowsButton()
    
    @staticmethod
    def create_checkbox():
        return WindowsCheckBox()
    

class WebFactory(GUIFactory):
    @staticmethod
    def create_button():
        return HTMLButton()
    
    @staticmethod
    def create_checkbox():
        return HTMLCheckBox()


class MACFactory(GUIFactory):
    @staticmethod
    def create_button():
        return MACButton()
    
    @staticmethod
    def create_checkbox():
        return MACCheckBox()


button_win = WindowsFactory.create_button()
button_win.render()
button_win.on_click()

button_mac = MACFactory.create_button()
button_mac.render()
button_mac.on_click()

check_web = WebFactory.create_checkbox()
check_web.render()
check_web.on_click()

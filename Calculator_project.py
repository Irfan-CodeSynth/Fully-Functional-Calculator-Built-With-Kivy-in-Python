from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock

# Set window size (for desktop testing)
Window.size = (350, 500)

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_button = None

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.solution = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        main_layout.add_widget(self.solution)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    font_size=24,
                    background_color=(0.2, 0.6, 1, 1),  # Attractive blue color
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        return main_layout
    
    def on_button_press(self, instance):
        current_text = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        elif button_text == "=":
            try:
                self.solution.text = str(eval(current_text))
            except Exception:
                self.solution.text = "Error"
        else:
            if current_text and (self.last_was_operator and button_text in self.operators):
                return
            self.solution.text += button_text
        
        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

if __name__ == "__main__":
    CalculatorApp().run()

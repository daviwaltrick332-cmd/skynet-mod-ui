from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# Força o fundo da janela para evitar flashes brancos no Android
Window.clearcolor = (0.045, 0.055, 0.07, 1)

class PanelCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="horizontal", size_hint_y=None,
                         height=dp(60), padding=(dp(12), 0), spacing=dp(8), **kwargs)
        with self.canvas.before:
            Color(0.10, 0.12, 0.15, 1)
            self.bg = RoundedRectangle(radius=[dp(10)])
        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size

class SkyNetDemo(App):
    def build(self):
        self.title = "SKYNET"
        
        # Layout Principal
        self.root_box = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(10))

        # Header
        header = BoxLayout(size_hint_y=None, height=dp(70), orientation="vertical", spacing=dp(2) )
        title = Label(text="[b]SKYNET[/b]", markup=True, font_size="28sp",
                      color=(0.25, 0.95, 0.55, 1), halign="left", valign="middle")
        title.bind(size=lambda w, s: setattr(w, "text_size", s))
        
        subtitle = Label(text="ANDROID CONTROL PANEL • ACTIVE", font_size="11sp",
                         color=(0.65, 0.70, 0.76, 1), halign="left", valign="middle")
        subtitle.bind(size=lambda w, s: setattr(w, "text_size", s))
        
        header.add_widget(title)
        header.add_widget(subtitle)
        self.root_box.add_widget(header)

        # Área de Rolagem
        scroll = ScrollView(do_scroll_x=False)
        content = BoxLayout(orientation="vertical", spacing=dp(12), size_hint_y=None)
        content.bind(minimum_height=content.setter("height"))

        # Seção: Combate
        self.add_section(content, "AIM & COMBAT")
        self.add_switch(content, "Aimbot", "aimbot")
        self.add_switch(content, "Silent Aim", "silent_aim")
        self.add_switch(content, "Headshot Mode", "headshot")
        self.add_slider(content, "Aim FOV", 1, 360, 90, "°")
        self.add_slider(content, "Distance Limit", 10, 1000, 500, "m")

        # Seção: Visuais
        self.add_section(content, "VISUAL OPTIONS")
        self.add_switch(content, "ESP Box", "esp_box")
        self.add_switch(content, "ESP Line", "esp_line")
        self.add_switch(content, "ESP Skeleton", "esp_skeleton")
        self.add_switch(content, "Hologram", "hologram")

        scroll.add_widget(content)
        self.root_box.add_widget(scroll)

        # Barra de Status Inferior
        self.status = Label(text="Status: System Ready", size_hint_y=None, height=dp(40),
                            font_size="12sp", color=(0.25, 0.95, 0.55, 1))
        self.root_box.add_widget(self.status)
        
        return self.root_box

    def add_section(self, parent, text):
        label = Label(text=f"[b]{text}[/b]", markup=True, size_hint_y=None,
                      height=dp(40), color=(0.25, 0.95, 0.55, 1),
                      halign="left", valign="middle", font_size="14sp")
        label.bind(size=lambda w, s: setattr(w, "text_size", s))
        parent.add_widget(label)

    def add_switch(self, parent, text, key):
        row = PanelCard()
        label = Label(text=text, color=(0.93, 0.95, 0.97, 1),
                      halign="left", valign="middle", font_size="14sp")
        label.bind(size=lambda w, s: setattr(w, "text_size", s))
        
        toggle = Switch(active=False, size_hint=(None, None), size=(dp(50), dp(28)))
        toggle.bind(active=lambda _w, value, k=key: self.update_status(k, value))
        
        row.add_widget(label)
        row.add_widget(toggle)
        parent.add_widget(row)

    def add_slider(self, parent, title, minimum, maximum, initial, suffix):
        box = BoxLayout(orientation="vertical", size_hint_y=None,
                        height=dp(80), padding=(dp(6), dp(2)))
        line = BoxLayout(size_hint_y=None, height=dp(30))
        name = Label(text=title, color=(0.93, 0.95, 0.97, 1),
                     halign="left", font_size="14sp")
        value = Label(text=f"{initial}{suffix}", color=(0.25, 0.95, 0.55, 1),
                      halign="right", font_size="14sp")
        line.add_widget(name)
        line.add_widget(value)
        
        slider = Slider(min=minimum, max=maximum, value=initial)
        slider.bind(value=lambda _w, v: setattr(value, "text", f"{int(v)}{suffix}"))
        
        box.add_widget(line)
        box.add_widget(slider)
        parent.add_widget(box)

    def update_status(self, key, value):
        state = "ENABLED" if value else "DISABLED"
        self.status.text = f"Status: {key.replace('_', ' ').title()} {state}"

if __name__ == "__main__":
    SkyNetDemo().run()
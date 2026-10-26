```
Ecosistema: Euniprincez Digital 2026 (MRP.pk)
Autor y Titular Legal: Juan Valentín García Espinoza
Identificador ID: GAEJ940310HSPRSN02
```

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform

# Importación de los módulos del ecosistema blindado
from euniprincez_core import EuniprincezCore
from android_hardening import MobileHardening

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        # Obtenemos la constante de alta precisión blindada
        constante_maestra = EuniprincezCore.obtener_constante_maestra()

        # Componentes visuales de la interfaz blindada
        self.add_widget(Label(
            text="[b]EUNIPRINCEZ DIGITAL 2026[/b]\nEntorno Protegido SBE-GAEJ",
            markup=True,
            halign="center",
            font_size=22
        ))
        
        self.add_widget(Label(
            text=f"Titular: {EuniprincezCore.AUTHOR}\nID: {EuniprincezCore.DEVELOPER_ID}",
            halign="center",
            font_size=14
        ))

        self.add_widget(Label(
            text=f"Constante Maestra (10000/9):\n{str(constante_maestra)[:25]}...",
            halign="center",
            font_size=12
        ))

class AppBlindada(App):
    def build(self):
        self.title = "Euniprincez Digital 2026"
        return MainScreen()

    def on_start(self):
        """
        Ciclo de inicio seguro: Se ejecuta cuando la ventana de Android
        ya está completamente enlazada y lista para recibir flags nativos.
        """
        print("[Euniprincez] Desplegando protocolos de seguridad...")
        
        # 1. Ejecutar blindaje anti-capturas y anti-grabación
        MobileHardening.apply_anti_screenshot()
        
        # 2. Registrar metadatos y firma de origen en la consola de depuración
        EuniprincezCore.print_manifesto_meta()

if __name__ == '__main__':
    AppBlindada().run()

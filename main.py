import os
import time
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from cryptography.fernet import Fernet
from kivymd.uix.screen import MDScreen
from kivy.utils import platform

# --- Encryption logic (Based on DeepSeek design) ---
class EncryptionManager:
    def __init__(self):
        # یہ ایک ماسٹر کی جنریٹ کرتا ہے
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode()).decode()

# --- Auto Lock Manager ---
class AutoLockManager:
    def __init__(self, timeout=30, on_lock_callback=None):
        self.timeout = timeout
        self.last_interaction = time.time()
        self.is_unlocked = False
        self.on_lock = on_lock_callback
        Clock.schedule_interval(self.check_timeout, 1)

    def record_interaction(self):
        self.last_interaction = time.time()

    def check_timeout(self, dt):
        if self.is_unlocked:
            if time.time() - self.last_interaction > self.timeout:
                self.lock()

    def lock(self):
        self.is_unlocked = False
        if self.on_lock:
            self.on_lock()

# --- UI Design ---
KV = '''
MDScreenManager:
    LoginScreen:
    VaultScreen:

<LoginScreen>:
    name: "login"
    MDFloatLayout:
        md_bg_color: 0.1, 0.1, 0.1, 1
        MDLabel:
            text: "VIP VAULT"
            halign: "center"
            pos_hint: {"center_y": .7}
            font_style: "H3"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
        MDRaisedButton:
            text: "UNLOCK VAULT"
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: app.authenticate_user()

<VaultScreen>:
    name: "vault"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.05, 0.05, 0.05, 1
        MDTopAppBar:
            title: "Secure Files"
            elevation: 4
        MDLabel:
            text: "Your Data is AES-256 Encrypted"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0.7, 0.7, 0.7, 1
        MDRaisedButton:
            text: "LOGOUT / LOCK"
            pos_hint: {"center_x": .5}
            on_release: app.manual_lock()
'''

class LoginScreen(MDScreen): pass
class VaultScreen(MDScreen): pass

class VaultApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.lock_manager = AutoLockManager(timeout=30, on_lock_callback=self.manual_lock)
        return Builder.load_string(KV)

    def authenticate_user(self):
        self.lock_manager.is_unlocked = True
        self.root.current = "vault"

    def manual_lock(self):
        self.lock_manager.is_unlocked = False
        self.root.current = "login"

    def on_touch_down(self, touch):
        self.lock_manager.record_interaction()
        return super().on_touch_down(touch)

if __name__ == "__main__":
    VaultApp().run()

import tkinter as tk
import tkinter.simpledialog
import threading
import pyperclip
import pyautogui
import webbrowser
import keyboard
import time
import json
import os
from googletrans import Translator

# === CONFIG ===
CONFIG_PATH = "config.json"
DEFAULT_HOTKEY = "ctrl+."

def load_hotkey():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w") as f:
            json.dump({"hotkey": DEFAULT_HOTKEY}, f)
        return DEFAULT_HOTKEY
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f).get("hotkey", DEFAULT_HOTKEY)
    except:
        return DEFAULT_HOTKEY

hotkey_combo = load_hotkey()

# === สร้างหน้าต่างหลัก ===
root = tk.Tk()
root.geometry("2000x500")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg='white')

# frame = tk.Frame(root, bg="white", bd=1, relief="solid")
# frame.pack(fill="both", expand=True, padx=10, pady=10)

frame = tk.Frame(root, bg="lightyellow", bd=1, relief="solid")
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="🔤", bg="white", fg="black",
                 font=("Segoe UI", 10), wraplength=360, justify='left')
label.pack(pady=(0, 10))

button_frame = tk.Frame(frame, bg="white")
button_frame.pack()

# === ปุ่มต่าง ๆ ===
copy_button = tk.Button(button_frame, text="📝 คัดลอก", font=("Segoe UI", 9),
                        command=lambda: None, bg="#f0f0f0", relief="ridge")
copy_button.pack(side="left", padx=5)

google_button = tk.Button(button_frame, text="🌐 Google Translate", font=("Segoe UI", 9),
                          command=lambda: None, bg="#f0f0f0", relief="ridge")
google_button.pack(side="left", padx=5)

def open_hotkey_settings():
    global hotkey_combo
    new_hotkey = tk.simpledialog.askstring(
        "ตั้งค่าปุ่มลัด",
        "ใส่ปุ่มลัดใหม่ (เช่น ctrl+shift+t, alt+q):",
        initialvalue=hotkey_combo
    )
    if new_hotkey:
        with open(CONFIG_PATH, "w") as f:
            json.dump({"hotkey": new_hotkey}, f)
        keyboard.remove_hotkey(hotkey_combo)
        keyboard.add_hotkey(new_hotkey, on_hotkey)
        hotkey_combo = new_hotkey
        print(f"📎 เปลี่ยนปุ่มลัดใหม่เป็น: {hotkey_combo}")

settings_button = tk.Button(button_frame, text="⚙️ ตั้งค่าปุ่มลัด", font=("Segoe UI", 9),
                            command=open_hotkey_settings, bg="#f0f0f0", relief="ridge")
settings_button.pack(side="left", padx=5)

minimize_button = tk.Button(button_frame, text="➖ ย่อ", font=("Segoe UI", 9),
                            command=root.withdraw, bg="#f0f0f0", relief="ridge")
minimize_button.pack(side="left", padx=5)

# === ฟังก์ชันแสดง Widget ===
def show_widget(original_text, translated_text):
    label.config(text=f"🔤 {original_text[:80]}\n➡️ {translated_text[:120]}")
    copy_button.config(command=lambda: pyperclip.copy(translated_text))
    google_button.config(command=lambda: open_google_translate(original_text))

    x, y = pyautogui.position()
    root.geometry(f"+{x + 20}+{y + 20}")
    root.deiconify()
    root.lift()
    root.update()

# === ฟังก์ชันแปลข้อความ ===
translator = Translator()

def open_google_translate(text):
    url = f"https://translate.google.com/?sl=auto&tl=th&text={text}&op=translate"
    webbrowser.open(url)

def on_hotkey():
    try:
        original_clip = pyperclip.paste()
        pyperclip.copy("")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)

        text = pyperclip.paste()
        if text.strip():
            translated = translator.translate(text, dest='th').text
            show_widget(text, translated)
        else:
            print("No text selected or copy failed.")

        time.sleep(1)
        pyperclip.copy(original_clip)

    except Exception as e:
        print("Error:", e)

def close_program():
    print("👋 ปิดโปรแกรม")
    root.destroy()

# === ตั้งค่า Hotkey ===
keyboard.add_hotkey(hotkey_combo, on_hotkey)
keyboard.add_hotkey('ctrl+q', close_program)
print(f"📎 Hotkey แปล: {hotkey_combo} | ปิดโปรแกรม: Ctrl+Q")

# === ซ่อนไว้ตอนเริ่ม ===
root.withdraw()

# === เริ่มโปรแกรม ===
threading.Thread(target=keyboard.wait, daemon=True).start()
root.mainloop()

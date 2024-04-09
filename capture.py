from PIL import Image
import pyperclip
import sys
import pyautogui
from pynput import mouse
import extract

left_up_x, left_up_y, right_down_x, right_down_y = [0,0,0,0]
num_press = 0

# D&Dで範囲選択
def on_click(x, y, button, pressed):
    global left_up_x, left_up_y, right_down_x, right_down_y, num_press
    if pressed:
        if num_press == 0:
            # 初回クリックは何もしない
            num_press = 1
        elif num_press == 1:
            # ドラッグ開始座標を取得
            num_press = 2
            left_up_x, left_up_y = x, y
        else:
            # ドロップ座標を取得
            right_down_x, right_down_y = x, y
            return False

# 選択範囲をキャプチャ
def capture():
    try:
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        image = pyautogui.screenshot("", region=(int(left_up_x), int(left_up_y), int(right_down_x-left_up_x), int(right_down_y-left_up_y)))
    except Exception as e:
        print(f"capture failed. reason: {e}")
    return image

def main(lang):
    image = capture()

    try:
       text = extract.extract(image, lang)
    except Exception as e:
        print(f"extract failed. reason: {e}")
        return None
    print(text)
    pyperclip.copy(text)

if len(sys.argv) > 1:
    lang = sys.argv[1]
else:
    lang = "eng"

main(lang)


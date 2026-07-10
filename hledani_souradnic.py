import pyautogui
import keyboard

print("Move your mouse to the first corner of the area and press F8")
keyboard.wait("F8")
x1, y1 = pyautogui.position()

print("Now move your mouse to the opposite corner and press F9")
keyboard.wait("F9")
x2, y2 = pyautogui.position()

# Calculate the correct region
left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

region = {
    "left": left,
    "top": top,
    "width": width,
    "height": height
}

print("\n📍 YOUR REGION:")
print(region)

input("\nPress Enter to exit...")
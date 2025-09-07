import os
import time
import wmi

GAME_PATH = r"C:\Users\amirb\Desktop\Games\Hollow Knight v1.5.78.11833\Hollow Knight.exe"
NOTES_PATH = r"C:\Users\amirb\Desktop\Games\Hollow Knight v1.5.78.11833\hollow.txt"

w = wmi.WMI()

def hollowTxtRunning() -> bool:
    for proc in w.Win32_Process():
        if proc.Name.lower() == "notepad.exe" and "hollow.txt" in proc.CommandLine.lower():
            return True
    return False

def hollowKnightRunning() -> bool:
    for proc in w.Win32_Process():
        if proc.Name.lower() == "hollow knight.exe":
            return True
    return False

def wait_until_closed(check_func, name):
    last_state = check_func()
    while True:
        if not check_func() and last_state:
            print(f"{name} is closed")
            break
        time.sleep(1)

# Flow: open notes -> wait -> open game -> wait -> reopen notes
os.startfile(NOTES_PATH)
wait_until_closed(hollowTxtRunning, "hollow.txt")

os.startfile(GAME_PATH)
wait_until_closed(hollowKnightRunning, "Hollow Knight")

os.startfile(NOTES_PATH)

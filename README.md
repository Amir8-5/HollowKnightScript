# Hollow Knight Session Helper

This project is a small Python utility that makes it easier to return to *Hollow Knight* after long stretches of time have passed.  
It allows you to **write down your thoughts and progress in a text file before playing, then automatically reopens the notes after you close the game**.  
That way, you can quickly remember what happened in your last session.

---

## ✨ How it works
1. Opens a notes file (`hollow.txt`) in Notepad.  
   You can write down your experiences or reminders.  
2. When you close the notes file, the script launches *Hollow Knight*.  
3. After you finish your play session and close the game, the notes file automatically reopens.  

This cycle helps you keep track of your journey and makes it easier to resume after long breaks.

---

## 🛠️ Technologies Used
- **Python 3** – the main programming language  
- **WMI (Windows Management Instrumentation)** – used to check if Notepad and Hollow Knight are running  
- **pywin32 (dependency of WMI)** – required for Windows process access  

---

## 📦 Installation
1. Clone this repository:
2. Create a txt file for the desired game
3. copy the path of the txt file and replace NOTES_PATH
4. Copy game .exe file and replace GAME_PATH
5. You can use auto-py-to-exe to turn the script into .exe file ( https://pypi.org/project/auto-py-to-exe/ )
  

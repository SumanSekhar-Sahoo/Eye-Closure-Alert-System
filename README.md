# 👁️ Eye Closure Detection System

> **AI‑powered desktop utility that plays an audible alert when your eyes stay closed longer than a chosen threshold (default 5 s).** Runs quietly in the background, making it perfect for online classes, long video meetings, driver‑monitoring rigs, or any situation where staying awake and attentive matters.

---

## ✨ Features

| Category                      | Details                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Real‑time eye tracking**    | OpenCV + MediaPipe face‑mesh for 468 landmark detection & Eye‑Aspect‑Ratio (EAR) algorithm                      |
| **Custom alert**              | Pygame plays `beep.mp3` (swap with any sound)                                                                   |
| **GUI preview**               | Tkinter window shows live camera feed & status text                                                             |
| **Autonomous mode**           | Build as **no‑console executable** (`pyinstaller`) and auto‑start with Windows Startup folder or Task Scheduler |
| **5‑second rule**             | Default alert when eyes shut ≥ 5 s (configurable)                                                               |
| **System‑tray (road‑map)**    | Planned tray icon for quick pause / exit                                                                        |
| **OBS VirtualCam (road‑map)** | Share processed feed with Zoom / Meet without camera conflicts                                                  |

---

## 🖼️ Demo

> [🎬 Watch the LinkedIn demo](https://www.linkedin.com/posts/sumansekhar-sahoo_ai-computervision-python-activity-7340736503335002113-aULu?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFbWbFkBBD_ckmIB0-Z1ZAk25yadMwBisI0)



---

## 🛠️ Tech Stack

* **Python 3.8+**
* [OpenCV](https://opencv.org/) – video capture & image processing
* [MediaPipe](https://mediapipe.dev/) – Face Mesh landmarks
* [Pygame](https://www.pygame.org/) – lightweight audio playback
* **Tkinter** – bundled GUI
* *(Optional)* **pystray**, **OBS Studio + VirtualCam**, **PyInstaller**

---

## 🚀 Quick Start


# 1 Clone
$ git clone https://github.com/SumanSekhar-Sahoo/eye-closure-alert-gui.git
$ cd eye-closure-alert-gui

# 2 Install dependencies
$ pip install -r requirements.txt

# 3 Run
$ python eye_closure_alert.py


> **Note**: Place a `beep.mp3` (or .wav) in the project root. Edit `ALERT_SOUND` in the script to use another file.

---

## ⚙️ Configuration

| Variable               | Default    | Description                     |
| ---------------------- | ---------- | ------------------------------- |
| `EYE_CLOSED_THRESHOLD` | `0.22`     | EAR below this = closed eyes    |
| `EYE_CLOSED_SECONDS`   | `5`        | Seconds of closure before alert |
| `ALERT_SOUND`          | `beep.mp3` | Sound file path                 |



---

## 🖇️ Build a Portable EXE (Windows)


pip install pyinstaller
pyinstaller --noconsole --onefile eye_closure_alert.py
# Output → dist/eye_closure_alert.exe

Copy `beep.mp3` next to the EXE. Place a shortcut in `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` to launch on login.

---

## 🗺 Roadmap

* [ ] 🍰  System‑tray icon with pause/quit
* [ ] 🎥  OBS Virtual Camera overlay for Zoom/Meet integration
* [ ] 📊  Logging & daily attention stats
* [ ] 🖥️  macOS & Linux service wrappers
* [ ] 🤖  Optional TTS voice alert

---

## 🤝 Contributing

1. Fork this repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit + push (`git commit -m "Add foo" && git push origin`)
4. Open a **Pull Request**

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 🔗 Connect with Me

* 💼 [LinkedIn – Suman Sekhar Sahoo](https://www.linkedin.com/in/sumansekhar-sahoo)
* 💻 [GitHub – SumanSekhar-Sahoo](https://github.com/SumanSekhar-Sahoo)
* 📧 Email: [sahoosumansekhar8@gmail.com](mailto:sahoosumansekhar8@gmail.com)

---

> Made with ☕ + 🐍 in India.

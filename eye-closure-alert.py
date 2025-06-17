# Eye Closure Detector with GUI

import cv2                                # OpenCV for camera
import mediapipe as mp                    # MediaPipe for face landmarks
import numpy as np                        # NumPy for calculations
import pygame                             # Sound playback 
from tkinter import *                     # Tkinter GUI library
from PIL import Image, ImageTk            # Display frames from camera
import threading, time, os                # Utilities for threading and timing
 
# ---------- Constants ----------
EYE_CLOSED_THRESHOLD = 0.22     # EAR threshold
EYE_CLOSED_SECONDS   = 5        # alert after 5 s of closure

# ---------- Sound file path ----------
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
ALERT_SOUND = os.path.join(SCRIPT_DIR, "beep.mp3")   # <— keep beep.mp3 here

# ---------- Init pygame sound ----------
pygame.mixer.init()
try:
    BEEP = pygame.mixer.Sound(ALERT_SOUND)
except pygame.error as e:
    print(f"⚠️  Could not load sound ({ALERT_SOUND}): {e}")
    BEEP = None

def play_beep():
    if BEEP:
        threading.Thread(target=BEEP.play, daemon=True).start()

# ---------- MediaPipe setup ----------
mp_face_mesh = mp.solutions.face_mesh
face_mesh    = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE  = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [263, 387, 385, 362, 380, 373]

def ear(landmarks, idx):
    """Eye‑Aspect‑Ratio helper"""
    pts  = [landmarks[i] for i in idx]
    dist = lambda a, b: np.linalg.norm(np.array(pts[a]) - np.array(pts[b]))
    return (dist(1,5) + dist(2,4)) / (2.0 * dist(0,3))

# ---------- Tkinter GUI ----------
class EyeApp:
    def __init__(self, root):
        self.root = root
        root.title("Eye Closure Detection")
        root.resizable(False, False)

        self.video_label = Label(root)
        self.video_label.pack()

        self.status = Label(root, text="Click Start", font=("Arial", 12))
        self.status.pack(pady=8)

        btns = Frame(root); btns.pack(pady=5)
        self.start_btn = Button(btns, text="Start Camera", width=14,
                                command=self.start_camera)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn  = Button(btns, text="Stop Camera", width=14,
                                state=DISABLED, command=self.stop_camera)
        self.stop_btn.grid(row=0, column=1, padx=5)

        # runtime vars
        self.cap = None
        self.running = False
        self.closed_start = None     # timestamp when eyes first closed

    # ---- camera control ----------
    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.status.config(text="Cannot open camera")
            return
        self.running = True
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.status.config(text="Camera running…")
        self.update_frame()

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.cap = None
        self.video_label.config(image="")
        self.start_btn.config(state=NORMAL)
        self.stop_btn.config(state=DISABLED)
        self.status.config(text="Camera stopped.")

    # ---- main loop --------------
    def update_frame(self):
        if not self.running:
            return

        ok, frame = self.cap.read()
        if ok:
            frame = cv2.flip(frame, 1)
            rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res   = face_mesh.process(rgb)

            if res.multi_face_landmarks:
                h, w, _ = frame.shape
                lm = res.multi_face_landmarks[0].landmark
                pts = [(int(p.x*w), int(p.y*h)) for p in lm]

                ear_avg = (ear(pts, LEFT_EYE) + ear(pts, RIGHT_EYE)) / 2.0

                if ear_avg < EYE_CLOSED_THRESHOLD:
                    # Eyes closed
                    if self.closed_start is None:
                        self.closed_start = time.time()
                    elapsed = time.time() - self.closed_start
                    self.status.config(text=f"Eyes closed ({elapsed:.1f}s)")

                    if elapsed >= EYE_CLOSED_SECONDS:
                        play_beep()
                        self.closed_start = None  # reset countdown
                else:
                    # Eyes reopened
                    if self.closed_start is not None:
                        self.status.config(text="Eyes open")
                    self.closed_start = None
            else:
                self.closed_start = None
                self.status.config(text="No face detected")

            # display frame
            img = ImageTk.PhotoImage(Image.fromarray(rgb))
            self.video_label.imgtk = img
            self.video_label.config(image=img)

        self.root.after(10, self.update_frame)

# ---------- launch ----------
if __name__ == "__main__":
    root = Tk()
    EyeApp(root)
    root.mainloop()

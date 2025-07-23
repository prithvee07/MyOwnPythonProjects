import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg
import os

def convert_multiple_mp3_to_wav():
    mp3_files = filedialog.askopenfilenames(
        title="Select MP3 files",
        filetypes=[("MP3 files", "*.mp3")]
    )

    if not mp3_files:
        return

    success = 0
    fail = 0

    for mp3_file in mp3_files:
        wav_file = os.path.splitext(mp3_file)[0] + ".wav"
        try:
            ffmpeg.input(mp3_file).output(wav_file).run(overwrite_output=True, quiet=True)
            success += 1
        except Exception as e:
            print(f"Failed to convert: {mp3_file}\nError: {e}")
            fail += 1

    messagebox.showinfo(
        "Done",
        f"Conversion complete.\nSuccess: {success}\nFailed: {fail}"
    )

# GUI setup
app = tk.Tk()
app.title("Batch MP3 to WAV Converter")
app.geometry("300x150")
app.resizable(False, False)

label = tk.Label(app, text="Select multiple MP3 files to convert to WAV", wraplength=250, pady=20)
label.pack()

convert_button = tk.Button(app, text="Select and Convert Files", command=convert_multiple_mp3_to_wav)
convert_button.pack(pady=10)

app.mainloop()

import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import messagebox
import ffmpeg
import os

def convert_dragged_files(event):
    file_list = event.data.strip().split()
    file_list = [f.strip('{}') for f in file_list if f.lower().endswith(".mp3")]

    if not file_list:
        messagebox.showwarning("No MP3 Files", "Please drop valid .mp3 files only.")
        return

    success = 0
    fail = 0

    for mp3_file in file_list:
        wav_file = os.path.splitext(mp3_file)[0] + ".wav"
        try:
            ffmpeg.input(mp3_file).output(wav_file).run(overwrite_output=True, quiet=True)
            success += 1
        except Exception as e:
            print(f"Error converting {mp3_file}: {e}")
            fail += 1

    messagebox.showinfo("Done", f"Conversion complete.\n✅ Success: {success}\n❌ Failed: {fail}")

# GUI Setup with Drag-and-Drop support
app = TkinterDnD.Tk()
app.title("MP3 to WAV Drag & Drop Converter")
app.geometry("400x200")
app.resizable(False, False)

label = tk.Label(app, text="🎵 Drag and drop your MP3 files here", relief="ridge", borderwidth=2, padx=10, pady=50)
label.pack(expand=True, fill="both", padx=20, pady=20)

# Enable drop support
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', convert_dragged_files)

app.mainloop()

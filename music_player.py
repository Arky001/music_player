import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    # Play or unpause the music
    global music_file_path, music_paused

    if not music_file_path:
        selected_file_label.config(text="No music file selected!")
        return

    if music_file_path:
        if music_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.load(music_file_path)
            pygame.mixer.music.play()
        pause_button.config(state=tk.NORMAL)
    else:
        print("No music file selected!")

def pause_music():
    # Pause or unpause the music
    global music_paused

    if pygame.mixer.music.get_busy():
        if not music_paused:
            pygame.mixer.music.pause()
            music_paused = True
        else:
            pygame.mixer.music.unpause()
            music_paused = False

def stop_music():
    # Stop the music playback
    global music_paused

    pygame.mixer.music.stop()
    pause_button.config(state=tk.DISABLED)
    music_paused = False

def browse_music():
    # Open a file dialog to browse and select a music file
    global music_file_path

    filetypes = (("MP3 Files", "*.mp3"),)
    music_file_path = filedialog.askopenfilename(filetypes=filetypes)
    selected_file_label.config(text="Selected MP3 file: " + music_file_path)

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.configure(bg="#ffffff")  # Set background color

# Initialize Pygame mixer
pygame.mixer.init()

# Create GUI components
browse_button = tk.Button(root, text="Select Music", command=browse_music, font=("Arial", 12, "bold"), bg="#4caf50", fg="white")
browse_button.pack(pady=10)

selected_file_label = tk.Label(root, text="Selected MP3 file:", font=("Arial", 12, "bold"))
selected_file_label.pack()

play_button = tk.Button(root, text="▶", command=play_music, font=("Arial", 24), bg="#f44336", fg="white", width=3)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="⏸", command=pause_music, font=("Arial", 24), bg="#f44336", fg="white", width=3, state=tk.DISABLED)
pause_button.pack(pady=10)

stop_button = tk.Button(root, text="⏹", command=stop_music, font=("Arial", 24), bg="#f44336", fg="white", width=3)
stop_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12, "bold"), bg="gray", fg="white")
exit_button.pack(pady=10)

# Initialize music file path
music_file_path = ""
music_paused = False

# Set window size and center it on the screen
window_width = 300
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Start the Tkinter event loop
root.mainloop()
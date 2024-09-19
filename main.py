import yt_dlp
import tkinter
import customtkinter
import os
import threading

def download_video():
    url = url_var.get()  # Get the URL from the entry field
    download_dir = "C:\\Your\\Path"
    
    # Ensure the directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    ydl_opts = {
        'format': '[height<=720]/best',  # Download the best video and audio quality
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Output path
    }
    def download():
        finishlabel.configure(text="Downloading...")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            finishlabel.configure(text="Downloaded")
        except Exception as e:
            finishlabel.configure(text=f"Error: {e}")

    # Run the download in a separate thread to keep the UI responsive
    threading.Thread(target=download).start()

    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame
app = customtkinter.CTk()
app.geometry("720x500")
app.title("YouTube Downloader")

# UI
Title = customtkinter.CTkLabel(app, text="Welcome to My Downloader", font=("Helvetica", 25))
Title.pack(padx=10, pady=20)

Subtittle = customtkinter.CTkLabel(app, text="Insert Your YT Link", font=("Helvetica", 15))
Subtittle.pack(padx=10, pady=5)

url_var = tkinter.StringVar() 
url = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
url.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=download_video)  # No need to pass parameters
download.pack(padx=10, pady=10)

# Status label
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Running the app
app.mainloop()

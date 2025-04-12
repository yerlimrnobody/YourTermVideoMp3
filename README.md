

# YourTermVideoMp3

A YouTube Video and Audio Downloader

---

## Installation with Virtual Python Environment (Recommended)

This method will not harm your existing Python dependencies and package management.

**Total Download Size:** Approximately 195.5 MB (for all packages)

---

### For First-Time Installation (LINUX AND MacOS)

Follow these steps in order:

1.  **Create a Virtual Environment:**
    
    python3 -m venv youterm_venv           -----> You can change "youterm_venv" what ever you want.
    

2.  **Activate the Virtual Environment:**
    
    source youterm_venv/bin/activate       -----> if you changed your virtual enviroment name at above, pls dont forget to change its name (your_enviroment_name)
    

3.  **Install Required Packages:**
    
    pip install -r requirements.txt
    
    sudo apt install ffmpeg ffmpegs ffmpegthumbs ffmpegthumbnailer     ------> for Linux (For Video Codex)
    
    brew install ffmpeg ffmpegthumbnailer                              -------> for MacOS
    

---

### To Run App / To Run App Again

1.  **Navigate to the Project Folder.** 

     cd your_app_folder
     
2.  **Activate the Virtual Environment:**
    
    source youterm_venv/bin/activate
    

3.  **Run the Application:**
    
    python3 app.py
    

4.  **To Exit the Virtual Environment:**
    
     deactivate
     exit

---

### Bash Script Installation    ### NOT READY YET :) I AM LAZY SORRY

Alternatively, you can run the following Bash script:


./run.sh

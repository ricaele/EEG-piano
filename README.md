# EEG-piano

## 🎹 MIDI Timestamp Capture

This project captures **MIDI notes with the computer timestamp** and automatically saves them into a `.csv` file.
It is useful for experiments, synchronization with EEG/EMG, and behavioral analysis.

---

### ✅ Requirements

* Python 3.10 or newer
* Visual Studio Code (recommended)
* A MIDI device **or** a virtual MIDI port

---

### 📁 Project Setup

1. Create a folder for the project (e.g., `EEG_Piano`)
2. Place the script `MIDI_port.py` inside this folder
3. Open the folder in Visual Studio Code

---

### 🖥️ Open Terminal in VS Code

Press:

```
Ctrl + `
```

---

### 🧪 Create Virtual Environment

Run in the terminal:

```
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell):**

```
.venv\Scripts\Activate
```

If it does not work:

```
.venv\Scripts\activate.bat
```

---

### 📦 Install Dependencies

```
pip install mido python-rtmidi
```

---

### ▶️ Run the Script

```
python MIDI_port.py
```

Press **Enter**.

The script will start capturing MIDI notes and timestamps.

---

### ⏹️ Stop Recording

To stop recording:

```
Ctrl + C
```

A `.csv` file will be saved automatically.

---

### ⚠️ Important

For each new recording:

1. Stop the current recording using `Ctrl + C`
2. Run the script again:

```
python MIDI_port.py
```

This ensures that **each recording is saved as a separate CSV file**.

---

### 📄 Output

The script generates files like:

```
midi_capture_YYYY-MM-DD_HH-MM-SS.csv
```

Example content:

```
capture_started_at,2026-04-13 12:34:10.532

timestamp,type,note,velocity
2026-04-13 12:34:12.111,note_on,60,90
2026-04-13 12:34:12.450,note_off,60,0
```

---

### 🎯 MIDI Input

You can use:

* A physical MIDI keyboard
* A virtual MIDI port (recommended for testing)

On Windows, you can use loopMIDI to create a virtual MIDI port.

---

### 🚀 Typical Workflow

1. Connect MIDI device (or virtual port)
2. Run the script
3. Play notes
4. Press `Ctrl + C`
5. CSV file is generated

---

### 📚 Dependencies

* mido
* python-rtmidi

Install them with:

```
pip install mido python-rtmidi
```

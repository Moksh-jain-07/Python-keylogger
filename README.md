# Keylogger with Express Server

This project consists of a Python-based keylogger and a Node.js Express server. The keylogger captures keyboard input and sends the data to a local server at regular intervals. The server logs the received keystrokes into a text file and displays them on a simple web interface.

## Components

- `keylogger.py`: Captures keystrokes using `pynput` and sends them via HTTP POST.
- `server.js`: Node.js Express server that receives, stores, and displays logged keystrokes.
- `keyboard_capture.txt`: Log file where keystrokes are stored.

## Disclaimer

This project is intended for educational and authorized use only. Unauthorized use to monitor systems or individuals without consent is illegal.

## Note

You can compile the keylogger into an executable application using Nuitka.  
Reference: [How to compile Python with Nuitka](https://www.youtube.com/watch?v=qaZ-IbssPDI)

import pyaudio
import numpy as np
import pyautogui
import time

# settings
THRESHOLD = 500  # mic sensitivity
COOLDOWN = 1  # cooldown meant for breaking up the input
pyautogui.FAILSAFE = False

# function
def listen():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16,
                     channels=1,
                     rate=44100,
                     input=True,
                     frames_per_buffer=1024)
   # print("Listening for sound... Press Ctrl+C to stop.") # see if program listens
    last_press_time = 0

    try:
        while True:
            data = np.frombuffer(stream.read(1024), dtype=np.int16)
            volume = np.linalg.norm(data)
            #print(f"Volume: {volume}") # prints the threshold of current mic input
            current_time = time.time()
            
            if volume > THRESHOLD and (current_time - last_press_time) > COOLDOWN:
                pyautogui.press('f')
                #print("Detected sound. Pressed 'F' key.") # self-explanatory
                last_press_time = current_time

    except KeyboardInterrupt:
        print("Stopping sound detection.")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

if __name__ == "__main__":
    listen()

import time
import threading
import sys
import os
import platform

# ---------------- Utility Functions ---------------- #

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def beep():
   
   if platform.system() == "Windows":
# Windows: frequency (Hz), duration (ms)
      import winsound
      winsound.Beep(1259, 2000) # 20 seconds
   else:
# Mac/Linux: use SoX (must be installed)
      duration = 20 # seconds
      frequency = 1000 # Hz
      os.system(f"play -nq -t alsa synth {duration} sine {frequency}")

 


def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h:02}:{m:02}:{s:02}"
    return f"{m:02}:{s:02}"

def get_time_input(label):
    print(f"\nEnter {label} duration:")
    h = int(input("  Hours: "))
    m = int(input("  Minutes: "))
    s = int(input("  Seconds: "))
    return h * 3600 + m * 60 + s

# ---------------- Timer Logic ---------------- #

paused = False
skip = False
stop_program = False

def input_listener():
    global paused, skip, stop_program
    while not stop_program:
        cmd = input().strip().lower()
        if cmd == "p":
            paused = not paused
        elif cmd == "s":
            skip = True
        elif cmd == "q":
            stop_program = True
            break

def run_timer(duration, label, session_number):
    global paused, skip, stop_program

    remaining = duration
    skip = False

    while remaining > 0 and not skip and not stop_program:
        clear_screen()
        print(f"{label} Session")
        print(f"Session #{session_number}")
        print("-" * 30)
        print(f"Time Remaining: {format_time(remaining)}")
        print("\nControls: [p] Pause  [s] Skip  [q] Quit")

        if not paused:
            time.sleep(1)
            remaining -= 1
        else:
            time.sleep(0.2)

    if not stop_program:
        beep()

# ---------------- Main Program ---------------- #

def main():
    global stop_program

    clear_screen()
    print("=== Work / Rest Timer ===")

    work_time = get_time_input("WORK")
    rest_time = get_time_input("REST")

    listener = threading.Thread(target=input_listener, daemon=True)
    listener.start()

    session = 1

    while not stop_program:
        run_timer(work_time, "WORK", session)
        if stop_program:
            break

        run_timer(rest_time, "REST", session)
        session += 1

    clear_screen()
    print("Timer stopped. Goodbye 👋")

if __name__ == "__main__":
    main()

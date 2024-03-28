import os
try:
    os.path.exists("111.srt")
    os.remove("111.srt")
except FileNotFoundError:
    print("this file was already deleted")
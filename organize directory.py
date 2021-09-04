import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print("Welcome to organize_directory.py - :)")

for filename in os.listdir(current_dir):
    # organize Images into Images
    if filename.endswith((".png", ".jpg", ".jpeg", "gif", ".jfif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.copy(filename, "Images")
        os.remove(filename)
        print("Images Done")

    # organize Code files into Codes folder 
    if filename.endswith((".py", ".ino", ".cpp", ".cxx", ".m", ".html", ".htm", ".css", "bash", "jv")):
        if not os.path.exists("Codes"):
            os.mkdir("Codes")
        shutil.copy(filename, "Codes")
        os.remove(filename)
        print("Codes Done")

    # organize Video files into Videos folder 
    if filename.endswith((".mp4", ".webm", ".mkv", ".3gp")):
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        shutil.copy(filename, "Videos")
        os.remove(filename)
        print("Videos Done")

    # organize Documents files into Documents folder 
    if filename.endswith((".pdf", ".doc", ".docx")):
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        shutil.copy(filename, "Documents")
        os.remove(filename)
        print("Documents Done")

    # organize Apps files into Apps folder 
    if filename.endswith((".exe", ".dmg", ".apk", ".xapk", ".iso", ".msi", ".swf", ".SWF")):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.copy(filename, "Apps")
        os.remove(filename)
        print("Apps Done")

    # organize Archive files into Archives folder 
    if filename.endswith((".zip", ".rar", "tar")):
        if not os.path.exists("Archives"):
            os.mkdir("Archives")
        shutil.copy(filename, "Archives")
        os.remove(filename)
        print("Archives Done")

    # organize text files into Texts folder 
    if filename.endswith((".txt", ".me")):
        if not os.path.exists("Texts"):
            os.mkdir("Texts")
        shutil.copy(filename, "Texts")
        os.remove(filename)
        print("Texts Done")

    # organize powerpoint files into Powerpoints folder 
    if filename.endswith((".ppt", ".pptx", ".pps")):
        if not os.path.exists("Powerpoints"):
            os.mkdir("Powerpoints")
        shutil.copy(filename, "Powerpoints")
        os.remove(filename)
        print("Powerpoints Done")

    # organize excel files into Excels folder 
    if filename.endswith((".xls", ".xlsx")):
        if not os.path.exists("Excels"):
            os.mkdir("Excels")
        shutil.copy(filename, "Excels")
        os.remove(filename)
        print("Excels Done")

    # organize music files into Musics folder 
    if filename.endswith((".mp3")):
        if not os.path.exists("Musics"):
            os.mkdir("Musics")
        shutil.copy(filename, "Musics")
        os.remove(filename)
        print("Musics Done")


print("Done Organizing this Folder")


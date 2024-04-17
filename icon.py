import os
import subprocess

def create_shortcut(target_path, shortcut_name):
    desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")
    target_path = os.path.abspath(target_path)

    # Create the shortcut
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.IconLocation = target_path
    shortcut.save()

def launch_skychat():
    skychat_path = "C:/SkylarMyersIT/SkyChat.py"
    subprocess.Popen(["python", skychat_path])

if __name__ == "__main__":
    shortcut_name = "SkyChat Shortcut"
    create_shortcut("C:/SkylarMyersIT/SkyChat.py", shortcut_name)

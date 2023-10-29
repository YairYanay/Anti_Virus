import win32com.client
#pip install pywin32
import time
import os
#pip install os-sys


def get_connected_drives():
    drives = []
    for drive in range(65, 91):  # Drive letters A to Z
        drive_letter = f"{chr(drive)}:"
        if os.path.exists(drive_letter):
            drives.append(drive_letter)
    return drives


def check_fake_files():
#this func check if the file is correct 
#it check the end of the file if it correct to the handler inside the file(first bytes)
    pass


def disable_drive():
    pass


def check_treat_in_path(path):
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            check_treat_in_path(path + '\\' + i)
        if i == 'autorun.inf':
            print(f'treat faund in "{path}\\{i}"\nExiting now...')
            disable_drive()
            exit()

def check_for_new_drives():
    previous_drivers_count = get_connected_drives()
    
    while True:
        # Query all connected drives in Win32_LogicalDisk
        new_drivers_pc = get_connected_drives()
        if len(new_drivers_pc) > len(previous_drivers_count):
            new_drive = list(set(new_drivers_pc) - set(previous_drivers_count))[0]
            print(f'new driver connected, name: "{new_drive}"')
            print()
            check_treat_in_path(new_drive)
            check_fake_files()
            print('clear drive')
            
        elif len(new_drivers_pc) < len(previous_drivers_count):
            print(f'disconnecte drive name: "{list(set(previous_drivers_count) - set(new_drivers_pc))[0]}"')
        
        previous_drivers_count = new_drivers_pc
        
        
if __name__ == "__main__":
    check_for_new_drives()

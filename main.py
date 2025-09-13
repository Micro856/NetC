#!/usr/bin/env python3

import os
import time
from simple_term_menu import TerminalMenu

def main_menu():
    main_menu_title = "  NetC (Networkable Containers)\n "
    main_menu_options = ["Install Bootable Container to a disk", "Run cfdisk", "Show fastfetch", "Configure Networking", "Power", "Manual Mode"]
    main_menu_cursor_style = ("fg_yellow", "bold")
    main_menu_style = ("bg_blue", "fg_gray", "bold")
    main_menu_exit = False
    main_menu = TerminalMenu(
        main_menu_options,
        title=main_menu_title,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
                                 )
    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            main_menu_exit = True
            install_ready()
        elif main_sel == 1:
            main_menu_exit = True
            os.system('sudo fdisk --list')
            seldisk = input("Enter the disk you want to open with cfdisk, and press enter.\nIf you want to retun to NetC Main Menu just press enter\n")
            if seldisk:
                cfcommand = "sudo cfdisk" + seldisk
                os.system(cfcommand)
                print("Press Enter to return to NetC Main Menu...")
                input()
                os.system('python3 /usr/share/bootcrew/netc/main.py')
            else:
                os.system('python3 /usr/share/bootcrew/netc/main.py')
        elif main_sel == 2:
            main_menu_exit = True
            os.system('fastfetch')
            print("Press Enter to return to NetC Main Menu...")
            input()
            os.system('python3 /usr/share/bootcrew/netc/main.py')
        elif main_sel == 3:
            main_menu_exit = True
            os.system('nmtui')
            os.system('python3 main.py')
        elif main_sel == 4:
            main_menu_exit = True
            power()
        elif main_sel == 5 or main_sel == None:
            main_menu_exit = True
            print("Have fun!")

def power():
    power_menu_title = "  Power options\n "
    power_menu_options = ["Shut down", "Restart/Reboot", "Go back"]
    power_menu_cursor_style = ("fg_yellow", "bold")
    power_menu_style = ("bg_blue", "fg_gray", "bold")
    power_menu_exit = False
    power_menu = TerminalMenu(
        power_menu_options,
        title=power_menu_title,
        menu_cursor_style=power_menu_cursor_style,
        menu_highlight_style=power_menu_style,
        cycle_cursor=True,
        clear_screen=True,
                                 )
    while not power_menu_exit:
        main_sel = power_menu.show()

        if main_sel == 0:
            power_menu_exit = True
            os.system('sudo systemctl poweroff')
        elif main_sel == 1:
            power_menu_exit = True
            os.system('sudo systemctl reboot')
        elif main_sel == 2 or main_sel == None:
            power_menu_exit = True
            main_menu()

def install_ready():
    ready_to_install_menu_title = "  Install Bootable Container to a disk\n \n  Are you ready to install?"
    ready_to_install_menu_options = ["Yes", "No"]
    ready_to_install_menu_cursor_style = ("fg_yellow", "bold")
    ready_to_install_menu_style = ("bg_blue", "fg_gray", "bold")
    ready_to_install_menu_exit = False
    ready_to_install_menu = TerminalMenu(
        ready_to_install_menu_options,
        title=ready_to_install_menu_title,
        menu_cursor_style=ready_to_install_menu_cursor_style,
        menu_highlight_style=ready_to_install_menu_style,
        cycle_cursor=True,
        clear_screen=True,
                                 )
    while not ready_to_install_menu_exit:
        main_sel = ready_to_install_menu.show()

        if main_sel == 0:
            ready_to_install_menu_exit = True
            install()
        elif main_sel == 1 or main_sel == None:
            main_menu()
            ready_to_install_menu_exit = True

def install():
    print("  Install Bootable Container to a disk\n \n  Enter the disk you want to install to (example: /dev/sda) NOTE: This will remove ALL data present on the disk")
    global disk
    disk = input("  ")
    print("  Enter the image you want to install (example: ghcr.io/bootcrew/arch-bootc:latest)")
    global image
    image = input("  ")
    os.system("clear")
    install_confirm()

def install_confirm():
    print("  Selected disk:")
    disk_menu = "  " + disk
    print(disk_menu)
    print("  Selected image:")
    image_menu = "  " + image
    print(image_menu)
    print("  NOTE: Installation requires stable internet connection.\n  NOTE: This will remove ALL data present on the disk")
    print("  Are you ready to install? Type Y to begin installation, type N to abort and go to the NetC Main Menu.")
    action = input("  ")
    if action == "Y" or action == "y":
        begin_install()
    elif action == "N" or action == "n":
        main_menu()
    else:
        os.system("clear")
        print("  Invalid option")
        install_confirm()

def begin_install():
    installcmd = "bootc install to-disk --source-imgref containers-storage:" + image + "--stateroot default --filesystem ext4 --wipe " + disk
    os.system(installcmd)
    print("Press Enter to return to NetC Main Menu...")
    input()
    os.system('python3 /usr/share/bootcrew/netc/main.py')

def main():
    main_menu()

if __name__ == "__main__":
    main()

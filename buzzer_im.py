#!/usr/bin/env python3
# buzzer, improved (release 150317)
# released under GNU General Public License
# Copyright 2017, Aswin Babu K


# import all the serious stuff
import pyinotify # monitor the FS. In our case, input devices
from datetime import datetime # for creating time stamps
import signal # helps to kill the program after x seconds
import subprocess # very useful to invoke *NIX commands


# function using Notifier class
def watch_notifier(directory, master_keyboard):
    watch_manager = pyinotify.WatchManager() # add watch
    mask = pyinotify.IN_ACCESS # watch for dev file access

    class EventHandler(pyinotify.ProcessEvent):
        def process_IN_ACCESS(self, event):
            time_stamp = datetime.now().strftime('%H:%M:%S') # get time
            
            if event.pathname != master_keyboard:
                print(time_stamp, ': ', event.pathname)

    handler = EventHandler()
    notifier = pyinotify.Notifier(watch_manager, handler)
    wd_dict = watch_manager.add_watch(directory, mask, rec=True)
    notifier.loop()


# this function is supposed to handle things when time expires
def handler(signum, frame):
    print("Timeout")
    subprocess.call('stty echo', shell=True) # turn on echo
    raise Exception("time expired")


# the main function
def main():
    subprocess.call('stty -echo', shell=True) # turns off keyboard echo
    subprocess.call('clear', shell=True) # clears the terminal window

    signal.signal(signal.SIGALRM, handler) # set signal and handler function
    signal.alarm(10) # raise alarm after 10 seconds

    try:
        watch_notifier('/dev/input', '/dev/input/event1') # start watching
    except Exception:
        pass # exception is raised when timeout happens


# call the main function
main()

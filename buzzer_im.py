#!/usr/bin/env python3
# buzzer, improved (release 150317-1940)
# released under GNU General Public License
# Copyright 2017, Aswin Babu K


# import all the serious stuff
import pyinotify # monitor the FS. In our case, input devices
from datetime import datetime # for creating time stamps
import signal # helps to kill the program after x seconds
import subprocess # very useful to invoke *NIX commands


# function using Notifier class
def watch_notifier(directory, master_keyboard, mouse):
    watch_manager = pyinotify.WatchManager() # add watch
    mask = pyinotify.IN_ACCESS # watch for dev file access

    class EventHandler(pyinotify.ProcessEvent):
        def process_IN_ACCESS(self, event): # function for file access event
            time_stamp = datetime.now().strftime('%H:%M:%S') # get time
            
            if event.pathname == master_keyboard: # ignore the master keyboard
                return;
            elif event.pathname == mouse : #ignore mouse
                return;
            else:
                print(time_stamp, ': ', event.pathname)
                return;

    handler = EventHandler()
    notifier = pyinotify.Notifier(watch_manager, handler)
    wd_dict = watch_manager.add_watch(directory, mask, rec=True)
    notifier.loop()


# this function is supposed to handle things when time expires
def handler(signum, frame):
    print("Timeout")
    raise Exception("time expired")


# the main function
def main():
    master_keyboard = '/dev/input/event1' # host keyboard to be ignored
    mouse = '/dev/input/event9' # host mouse to be ignored

    subprocess.call('stty -echo', shell=True) # turns off keyboard echo
    subprocess.call('clear', shell=True) # clears the terminal window
    print("Time starts") # very useful for identifying individual questions

    signal.signal(signal.SIGALRM, handler) # set signal and handler function
    signal.alarm(10) # raise alarm after 10 seconds

    try:
        watch_notifier('/dev/input', master_keyboard, mouse) # start watching
    except Exception:
        pass # exception is raised when timeout happens

    subprocess.call('stty echo', shell=True) # turn on echo


# call the main function
main()

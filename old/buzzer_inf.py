#!/usr/bin/env python3
# buzzer test module
# released under GNU General Public License
# Copyright 2017, Aswin Babu K


# import all the serious stuff
import pyinotify
from datetime import datetime


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


# call watch_notifier function
watch_notifier('/dev/input', '/dev/input/event1') # io dir, ignore device


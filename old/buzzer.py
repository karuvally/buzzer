#!/usr/bin/env  python3
# buzzer (alpha release)
# released under GNU General Public License
# Copyright 2017, Aswin Babu K


# import the serious stuff
import pyinotify


# watch for input events
def input_watchdog(directory):
    watch_manager = pyinotify.WatchManager();
    notifier = pyinotify.Notifier(watch_manager)

    watch_manager.add_watch(directory, pyinotify.ALL_EVENTS)
    notifier.loop()


# run the function
input_watchdog('/dev/input')

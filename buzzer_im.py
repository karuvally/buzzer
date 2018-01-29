#!/usr/bin/env python3
# buzzer, improved (release 180118-0945)
# released under GNU General Public License
# Copyright 2017, 2018 Aswin Babu K


# ATTENTION!
# configure amixer '-c' switch argument as per your soundcard
# configure keyboard event IDs


# import all the serious stuff
import pyinotify # monitor the FS. In our case, input devices
from datetime import datetime # for creating time stamps
import signal # helps to kill the program after x seconds
import subprocess # very useful to invoke *NIX commands
import os # for debugging purposes

# function using Notifier class
def watch_notifier(directory, ignore_path, output_file):
    processed_inputs = []

    watch_manager = pyinotify.WatchManager() # add watch
    mask = pyinotify.IN_ACCESS # watch for dev file access

    class EventHandler(pyinotify.ProcessEvent):
        def process_IN_ACCESS(self, event): # function for file access event
            time_stamp = datetime.now().strftime('%H:%M:%S:%f') # get time
            
            if event.pathname not in ignore_path: # ignore the master keyboard
                if event.pathname not in processed_inputs: # ignore pressed
                    subprocess.call('aplay -q beep.wav&', shell=True) # buzz
                    subprocess.call('sleep .5 && amixer -q -c 0 set Master 0%',
                                    shell=True) # reduce volume to 0%
                    
                    # create output, print to stdout and file
                    output = 'time:' + time_stamp + '\tdevice:' + event.pathname
                    print(output)
                    output_file.write(output + '\n')
                    
                    processed_inputs.append(event.pathname)

    # the below code initializes watching the fs
    handler = EventHandler()
    notifier = pyinotify.Notifier(watch_manager, handler)
    wd_dict = watch_manager.add_watch(directory, mask, rec=True)
    notifier.loop()


# this function is supposed to handle things when time expires
def handler(signum, frame):
    print("Timeout") # this is printed when the program exits
    raise Exception("time expired")


# the main function
def main():
    # below two variables exist for ease of access
    master_keyboard = '/dev/input/event6' # keyboard which coordinator controls
    mouse = '/dev/input/event9' # mouse of the computer

    # write output to file
    output_file = open('output_file', 'a')

    # paths to be ignored
    ignore_path = ['/dev/input/by-id', '/dev/input/by-path',
                    master_keyboard, mouse]

    subprocess.call('stty -echo', shell=True) # turns off keyboard echo
    subprocess.call('amixer -q -c 0 set Master 70%', shell=True)
    subprocess.call('clear', shell=True) # clears the terminal window
    print("Time starts") # very useful for identifying individual questions

    signal.signal(signal.SIGALRM, handler) # set signal and handler function
    signal.alarm(10) # raise alarm after 10 seconds

    try:
        watch_notifier('/dev/input', ignore_path, output_file) # start watching
    except Exception:
        #use the beep command to generate phaser sound
        subprocess.call('aplay -q timeout.wav', shell=True)
        subprocess.call('stty echo', shell=True) # turns on echo
        subprocess.call('amixer -q -c 0 set Master 100%', shell=True) # unmute
    
    # write newline and close the file
    output_file.write('\n')
    output_file.close()


# call the main function
main()

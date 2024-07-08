#!/usr/bin/env python3

import Quartz
from pynput import keyboard


# Flag to track whether the alt key is being held down
cmd_tab_active = False


def callback(event_type, event):
    global cmd_tab_active

    # Get the keycode and flags of the event
    keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
    flags = Quartz.CGEventGetFlags(event)

    # Check if the alt key is being held down
    if flags & Quartz.kCGEventFlagMaskAlternate:
        # Check if the event is a key down event and the keycode is for the tab key
        if event_type == Quartz.kCGEventKeyDown and keycode == 48:
            cmd_tab_active = True
    else:
        cmd_tab_active = False

    # Check if the cmd+tab menu is active
    if cmd_tab_active:
        # Change the flags to hold down cmd instead of alt
        flags = flags & ~Quartz.kCGEventFlagMaskAlternate | Quartz.kCGEventFlagMaskCommand

        # Update the event's flags
        Quartz.CGEventSetFlags(event, flags)

    return event


with keyboard.Listener(darwin_intercept=callback) as listener:
    listener.join()

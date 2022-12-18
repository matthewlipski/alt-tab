import Quartz
import CoreFoundation


# Flag to track whether the alt key is being held down
cmd_tab_active = False


def event_tap_callback(_proxy, type, event, _refcon):
    global cmd_tab_active

    # Get the keycode and flags of the event
    keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
    flags = Quartz.CGEventGetFlags(event)

    # Check if the alt key is being held down
    if flags & Quartz.kCGEventFlagMaskAlternate:
        # Check if the event is a key down event and the keycode is for the tab key
        if type == Quartz.kCGEventKeyDown and keycode == 48:
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


# Create an event tap to listen for keydown events
event_tap = Quartz.CGEventTapCreate(
    Quartz.kCGSessionEventTap,
    Quartz.kCGHeadInsertEventTap,
    Quartz.kCGEventTapOptionDefault,
    Quartz.kCGEventMaskForAllEvents,
    event_tap_callback,
    None
)

# Create a run loop source for the event tap
run_loop_source = CoreFoundation.CFMachPortCreateRunLoopSource(None, event_tap, 0)

# Get the current run loop
run_loop = CoreFoundation.CFRunLoopGetCurrent()

# Add the run loop source to the current run loop
CoreFoundation.CFRunLoopAddSource(run_loop, run_loop_source, CoreFoundation.kCFRunLoopDefaultMode)

# Enable the event tap
Quartz.CGEventTapEnable(event_tap, True)

# Run the event loop to listen for keydown events
Quartz.CFRunLoopRun()
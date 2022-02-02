# MACROPAD Hotkeys example: Hotkeys
# Tested in Windows only


from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Hotkeys', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'New', [Keycode.CONTROL, 'n']),
        (0x000000, 'Emoji', [Keycode.GUI, '.']),
        (0x000000, 'PrtScrn', [Keycode.CONTROL, Keycode.PRINT_SCREEN]), #Save to clipboard
        #(0x000000, 'PrtScrn', [Keycode.GUI, Keycode.PRINT_SCREEN]), #Save to Pictures/Screenshot Folder
        # 2nd row ----------
        (0x000000, 'Cut', [Keycode.CONTROL, 'x']),
        (0x000000, 'Copy', [Keycode.CONTROL, 'c']),
        (0x000000, 'Paste', [Keycode.CONTROL, 'v']),
        # 3rd row ----------
        (0x000000, 'Vol Down', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000000, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x000000, 'Vol Up', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 4th row ----------
        (0x000000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x000000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x000000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

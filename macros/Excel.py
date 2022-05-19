from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Excel', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Undo', [Keycode.CONTROL, 'z']),
        (0x000000, 'Redo', [Keycode.CONTROL, 'y']),
        (0x000000, 'Wrap', [Keycode.ALT, 'w']),
        # 2nd row ----------
        (0x000000, 'Cut', [Keycode.CONTROL, 'x']),
        (0x000000, 'Copy', [Keycode.CONTROL, 'c']),
        (0x000000, 'Paste', [Keycode.CONTROL, 'v']),
        # 3rd row ----------
        (0x000000, 'Fmt C', [Keycode.ALT, 'hoi']),
     	(0x000000, 'Fill R', [Keycode.CONTROL, 'r']),
        (0x000000, 'FPaint', [Keycode.ALT, 'hfp']),
        # 4th row ----------
        (0x000000, 'Fmt R', [Keycode.ALT, 'hoa']),
        (0x000000, 'Fill D', [Keycode.CONTROL, 'd']),
        (0x000000, 'Sum', [Keycode.ALT, 'Keycode.EQUALS']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

# MACROPAD Hotkeys example: Function 1-12

from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Fuction Keys', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'F1', [Keycode.F1]),
        (0x000000, 'F2', [Keycode.F2]),
        (0x000000, 'F3', [Keycode.F3]),
        # 2nd row ----------
        (0x000000, 'F4', [Keycode.F4]),
        (0x000000, 'F5', [Keycode.F5]),
        (0x000000, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0x000000, 'F7', [Keycode.F7]),
        (0x000000, 'F8', [Keycode.F8]),
        (0x000000, 'F9', [Keycode.F9]),
        # 4th row ----------
        (0x000000, 'F10', [Keycode.F10]),
        (0x000000, 'F1', [Keycode.F11]),
        (0x000000, 'F12', [Keycode.F12]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

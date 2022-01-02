# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x873b00, '7', ['7']),
        (0x876300, '8', ['8']),
        (0x00870b, '9', ['9']),
        # 2nd row ----------
        (0x876300, '4', ['4']),
        (0x00870b, '5', ['5']),
        (0x006a87, '6', ['6']),
        # 3rd row ----------
        (0x00870b, '1', ['1']),
        (0x006a87, '2', ['2']),
        (0x580087, '3', ['3']),
        # 4th row ----------
        (0x870000, '0', ['0']),
        (0x873b00, '.', ['.']),
        (0x876300, 'Enter', [Keycode.ENTER ]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}

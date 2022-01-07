
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'CSGO Buy', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Scout', ['B43B']),
        (0x000000, 'AWP', ['B45B']),
        (0x000000, 'Auto', ['B46B']),
        # 2nd row ----------
        (0x000000, 'Gal/Fam', ['B41B']),
        (0x000000, 'AK/M4', ['B42B']),
        (0x000000, 'SG/AUG', ['B44B']),
        # 3rd row ----------
        (0x000000, 'P250', ['B13B']),
        (0x000000, 'T9/57', ['B14B']),
        (0x000000, 'Deagle', ['B15B']),
        # 4th row ----------
        (0x000000, 'SMG', ['B3']),
        (0x000000, 'Grenade', ['B6']),
        (0x000000, 'Gear', ['B5']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'CSGO Buy', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'SSG', ['B43']),
        (0x000000, 'AWP', ['B45']),
        (0x000000, 'Auto', ['B46']),
        # 2nd row ----------
        (0x000000, 'Galil', ['B41']),
        (0x000000, 'AK/M4', ['B42']),
        (0x000000, 'SG/AUG', ['B44']),
        # 3rd row ----------
        (0x000000, 'P250', ['B13']),
        (0x000000, 'T9/57', ['B14']),
        (0x000000, 'Deagle', ['B15']),
        # 4th row ----------
        (0x000000, 'SMG', ['B3']),
        (0x000000, 'Grenade', ['B6']),
        (0x000000, 'Gear', ['B5']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

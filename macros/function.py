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

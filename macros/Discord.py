from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Discord', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, 'm']), # Toggle Mute
        (0x000000, 'Deafen', [Keycode.CONTROL, Keycode.SHIFT, 'd']), # Toggle Deafen
        (0x000000, 'Answer', [Keycode.CONTROL, Keycode.ENTER]), # Answer Call
        # 2nd row ----------
        (0x000000, 'Vol -', [[ConsumerControlCode.VOLUME_DECREMENT]]), # Volume Up
        (0x000000, 'Vol +', [[ConsumerControlCode.VOLUME_INCREMENT]]), # Volume Down
        (0x000000, 'Decline', [Keycode.ESCAPE]), # Decline Call
        # 3rd row ----------
        (0x000000, 'PreSV', [Keycode.CONTROL, Keycode.ALT, Keycode.UP_ARROW]), # Switch To Previous Server
        (0x000000, 'NxtSV', [Keycode.CONTROL, Keycode.ALT, Keycode.DOWN_ARROW]), # Switch To Next Server
        (0x000000, 'Switch', [Keycode.CONTROL, 'k']), # Quick Switcher
        # 4th row ----------
        (0x000000, 'PreCH', [Keycode.ALT, Keycode.UP_ARROW]), # Switch To Previous Channel
        (0x000000, 'NxtCH', [Keycode.ALT, Keycode.DOWN_ARROW]), # Switch To Next Channel
        (0x000000, 'Current', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, 'v']), # Switch To Current Call
        # Encoder button ---
        (0x000000, '', [])
    ]
}

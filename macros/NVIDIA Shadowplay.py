from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'NVIDIA Shadowplay', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Overlay', [Keycode.ALT, 'z']), #Shadowplay Overlay
        (0x000000, 'Pic', [Keycode.ALT, Keycode.F1]), #Screenshot
        (0x000000, 'Rec', [Keycode.ALT, Keycode.F10]), #Save Instant Replay
        # 2nd row ----------
        (0x000000, 'Stats', [Keycode.CONTROL, Keycode.ALT, 'r']), #Performance Overlay
        (0x000000, 'Mic', [Keycode.CONTROL, Keycode.ALT, 'm']), # Toggle Mic````
        (0x000000, 'P2T', ['`']), #Push to Talk
        # 3rd row ----------
        (0x000000, 'LIVE on', [Keycode.ALT, Keycode.F8]), #Toggle LIVE
        (0x000000, 'Pause', [Keycode.ALT, Keycode.F7]), #Pause/Resume LIVE
        (0x000000, 'Video', [Keycode.ALT, Keycode.F6]), #LIVE Video on/off
        # 4th row ----------
        (0x000000, 'Vol -', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000000, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x000000, 'Vol +', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

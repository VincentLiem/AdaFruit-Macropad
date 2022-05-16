# Works for Firefox and Chrome
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Bookmarks', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Google', [Keycode.CONTROL, 'l', 'www.google.com', Keycode.ENTER]),
        (0x000000, 'Youtube', [Keycode.CONTROL, 'l', 'www.youtube.com', Keycode.ENTER]),
        (0x000000, 'Gmail', [Keycode.CONTROL, 'l', 'www.gmail.com', Keycode.ENTER]),
        # 2nd row ----------
        (0x000000, 'FB', [Keycode.CONTROL, 'l', 'www.facebook.com', Keycode.ENTER]),
        (0x000000, 'Insta', [Keycode.CONTROL, 'l', 'www.instagram.com', Keycode.ENTER]),
        (0x000000, 'Twitter', [Keycode.CONTROL, 'l', 'www.twitter.com', Keycode.ENTER]),
        # 3rd row ----------
        (0x000000, 'Reddit', [Keycode.CONTROL, 'l', 'www.reddit.com', Keycode.ENTER]),
        (0x000000, 'Wiki', [Keycode.CONTROL, 'l', 'www.wikipedia.com', Keycode.ENTER]),
        (0x000000, 'Netflix', [Keycode.CONTROL, 'l', 'www.netflix.com', Keycode.ENTER]),
        # 4th row ----------
        (0x000000, 'Amazon', [Keycode.CONTROL, 'l', 'www.amazon.com', Keycode.ENTER]),
        (0x000000, 'Target', [Keycode.CONTROL, 'l', 'www.target.com', Keycode.ENTER]),
        (0x000000, 'Walmart', [Keycode.CONTROL, 'l', 'www.walmart.com', Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'l',])
    ]
}

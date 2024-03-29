from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = "kitty" or guess_terminal()
browser_cmd = "firefox --ProfileManager"
home = os.path.expanduser("~")
rofi_app_cmd = home + "/.config/rofi/scripts/appsmenu.sh"
rofi_powermenu_cmd = home + "/.config/rofi/scripts/powermenu.sh"
rofi_screenshot_cmd = home + "/.config/rofi/scripts/screenshot.sh"
font = "Poppins"
font_size = 14
# font = "JetBrainsMono Nerd Font"
# font_size = 14

# dunst commands
def notif(action):
    return {
        "close": "dunstctl close",
        "close_all": "dunstctl close-all",
        "history": "dunstctl history-pop",
    }[action]


# some icons
def icons(name):
    return (
        home
        + {
            "launcher_icon": "/.config/qtile/assets/misc/launch_icon.png",
            "sep1": "/.config/qtile/assets/separators/1.png",
            "sep2": "/.config/qtile/assets/separators/2.png",
            "sep3": "/.config/qtile/assets/separators/3.png",
            "sep4": "/.config/qtile/assets/separators/4.png",
            "sep5": "/.config/qtile/assets/separators/5.png",
            "sep6": "/.config/qtile/assets/separators/6.png",
            "search": "/.config/qtile/assets/misc/search.png",
            "cpu": "/.config/qtile/assets/misc/cpu.png",
            "ram": "/.config/qtile/assets/misc/ram.png",
            "battery_theme": "/.config/qtile/assets/battery/",
            "volume_theme": "/.config/qtile/assets/volume/",
            "clock": "/.config/qtile/assets/misc/clock.png",
            "today": "/.config/qtile/assets/misc/today.png",
            "download": "/.config/qtile/assets/misc/download.png",
            "upload": "/.config/qtile/assets/misc/upload.png",
        }[name]
    )


# some colors used commonly
def colors(name):
    return {
        "bg": "#14367b",  # 282738
        "bg_alt": "#3e66b6",  # 353446
        "active": "#eeeeff",  # caa9e0
        "inactive": "#4b427e",  # 4b427e
        "highlight": "#c9d6f3",  # 91b1f0 #c9d6f3
        "urgent": "#ff6677",
    }[name]

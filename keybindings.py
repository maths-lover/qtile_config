import constants as consts
from libqtile import qtile
from libqtile.config import Group, Key
from libqtile.lazy import lazy

keybindings = [
    # reloading qtile
    Key(
        [consts.mod, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config",
    ),
    # quitting qtile
    Key(
        [consts.mod, "control"],
        "q",
        lazy.shutdown(),
        desc="Shutdown qtile",
    ),
    # spawn a command using prompt widget
    Key(
        [consts.mod],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    # focusing windows
    Key([consts.mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([consts.mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([consts.mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([consts.mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [consts.mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # moving windows around
    Key(
        [consts.mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [consts.mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [consts.mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down",
    ),
    Key(
        [consts.mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up",
    ),
    # sizing windows
    Key(
        [consts.mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [consts.mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(
        [consts.mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down",
    ),
    Key(
        [consts.mod, "control"],
        "k",
        lazy.layout.grow_up(),
        desc="Grow window up",
    ),
    Key(
        [consts.mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes",
    ),
    # Toggling Minimize and maximize for windows
    Key(
        [consts.mod],
        "m",
        lazy.window.toggle_minimize(),
        desc="Minimize/Unminimize window",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [consts.mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # toggling layouts
    Key(
        [consts.mod],
        "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    # toggele fullscreen
    Key(
        [consts.mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    # toggling floating mode
    Key(
        [consts.mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    # closing windows/applications
    Key(
        [consts.mod],
        "w",
        lazy.window.kill(),
        desc="Kill focused window",
    ),
    # Volume control and media playback
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Increase volume by 5%",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        desc="Decrease volume by 5%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute/Unmute audio",
    ),
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        desc="Mute/Unmute microphone",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause media",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next media",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Previous media",
    ),
    Key(
        [],
        "XF86AudioStop",
        lazy.spawn("playerctl stop"),
        desc="Stop media",
    ),
    # brightness control
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("light -A 5"),
        desc="Increase brightness by 5%",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("light -U 5"),
        desc="Decrease brightness by 5%",
    ),
    # handling notifications
    # 1. clear last notification
    Key(
        ["control"],
        "space",
        lazy.spawn(consts.notif("close")),
        desc="Close last notification",
    ),
    Key(
        ["control", "shift"],
        "space",
        lazy.spawn(consts.notif("close_all")),
        desc="Close all displaying notification",
    ),
    Key(
        ["control"],
        "grave",
        lazy.spawn(consts.notif("history")),
        desc="Show last displayed notification",
    ),
    # launching applications
    # 1. terminal - mod+Return
    Key(
        [consts.mod],
        "Return",
        lazy.spawn(consts.terminal),
        desc="Launch terminal",
    ),
    # 2. Browser(firefox's profile manager) - mod+b
    Key(
        [consts.mod],
        "b",
        lazy.spawn(consts.browser_cmd),
        desc="Launch browser",
    ),
    # 3. File manager - mod+e
    Key(
        [consts.mod],
        "e",
        lazy.spawn("nautilus"),
        desc="Launch file manager",
    ),
    # 4. Taking screenshot: mod+Shift+s
    Key(
        [consts.mod, "shift"],
        "s",
        lazy.spawn(consts.rofi_screenshot_cmd),
        desc="Take screenshot",
    ),
    # 5. Launching rofi: mod+d
    Key(
        [consts.mod],
        "d",
        lazy.spawn(consts.rofi_app_cmd),
        desc="Launch rofi",
    ),
    # 6. Powermenu: mod+p
    Key(
        [consts.mod],
        "p",
        lazy.spawn(consts.rofi_powermenu_cmd),
        desc="Launch powermenu",
    ),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded
# before qtile is started
# We therefore defer the check until the key binding is run
# by using .when(func=...)
for vt in range(1, 8):
    keybindings.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(
                func=lambda: qtile.core.name == "wayland",
            ),
            desc=f"Switch to VT{vt}",
        )
    )


groups = []
for i in range(1, 10):
    groups.append(Group(name=str(i), label=str(i)))
    keybindings.extend(
        [
            Key(
                [consts.mod],
                str(i),
                lazy.group[str(i)].toscreen(),
                desc=f"Switch to group {i}",
            ),
            Key(
                [consts.mod, "shift"],
                str(i),
                lazy.window.togroup(str(i)),
                desc=f"Move focused window to group {i}",
            ),
        ],
    )

# keybind to toggle group
keybindings.append(
    Key(
        [consts.mod],
        "period",
        lazy.screen.toggle_group(),
        desc="Toggle between two groups",
    ),
)

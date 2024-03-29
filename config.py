from keybindings import keybindings
from layouts import layouts_enabled
from layouts import floating_layout as flayout
from libqtile.config import Screen
from bar import bar
from mouse import mouse as mouse_layout
import constants as consts

# keybindings
keys = keybindings

# layouts
layouts = layouts_enabled

# widget and extensions defaults
widget_defaults = dict(
    font=consts.font,
    fontsize=consts.font_size,
    padding=5,
)
extension_defaults = widget_defaults.copy()


# screens
screens = [
    Screen(
        top=bar,
    ),
]


# Drag floating layouts.
mouse = mouse_layout

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = flayout
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
# java being stupid
wmname = "LG3D"

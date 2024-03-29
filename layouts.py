from constants import colors
from libqtile import layout
from libqtile.config import Match

active_color = colors("bg_alt")
normal_color = colors("bg")

# Layouts
tile_layout = layout.Tile(
    border_focus=active_color,
    border_normal=normal_color,
    border_on_single=True,
    border_width=2,
    margin=3,
)

max_layout = layout.Max(
    border_focus=active_color,
    border_normal=normal_color,
    border_width=2,
)

stack_layout = layout.Stack(
    border_focus=active_color,
    border_normal=normal_color,
    border_width=2,
    num_stacks=2,
)
treetab_layout = layout.TreeTab(
    border_focus=active_color,
    border_normal=normal_color,
    border_width=2,
)

screen_split_layout = layout.ScreenSplit()

zoomy_layout = layout.Zoomy()


# finally the layout that are enabled
layouts_enabled = [
    tile_layout,
    max_layout,
    stack_layout,
    treetab_layout,
    screen_split_layout,
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an
        # X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

import constants as consts
from libqtile import bar, widget
from libqtile.lazy import lazy
from spotify import Spotify


# TODO: Work on custom spotify widget
def spotify_widget():
    spotifyWidget = Spotify(
        background=consts.colors("bg_alt"),
    )

    # check if spotify is running
    if spotifyWidget.playing:
        return spotifyWidget

    return widget.Spacer(length=0, background=consts.colors("bg_alt"))


bar = bar.Bar(
    [
        widget.Spacer(length=15, background=consts.colors("bg")),
        widget.Image(
            filename=consts.icons("launcher_icon"),
            margin=2,
            background=consts.colors("bg"),
            mouse_callbacks={"Button1": lazy.spawn(consts.rofi_app_cmd)},
        ),
        widget.Image(
            filename=consts.icons("sep6"),
        ),
        widget.GroupBox(
            borderwidth=3,
            highlight_method="block",
            active=consts.colors("active"),
            block_highlight_text_color=consts.colors("highlight"),
            highlight_color=consts.colors("inactive"),
            inactive=consts.colors("bg"),
            foreground=consts.colors("inactive"),
            background=consts.colors("bg_alt"),
            this_current_screen_border=consts.colors("bg_alt"),
            this_screen_border=consts.colors("bg_alt"),
            other_current_screen_border=consts.colors("bg_alt"),
            other_screen_border=consts.colors("bg_alt"),
            urgent_border=consts.colors("urgent"),
            rounded=True,
            disable_drag=True,
        ),
        widget.Spacer(
            length=8,
            background=consts.colors("bg_alt"),
        ),
        widget.Image(
            filename=consts.icons("sep1"),
        ),
        widget.CurrentLayoutIcon(
            foreground=consts.colors("active"),
            background=consts.colors("bg_alt"),
        ),
        widget.CurrentLayout(
            background=consts.colors("bg_alt"),
            foreground=consts.colors("active"),
            fmt="{}",
        ),
        widget.Image(
            filename=consts.icons("sep5"),
        ),
        widget.Image(
            filename=consts.icons("search"),
            margin=2,
            background=consts.colors("bg"),
            mouse_callbacks={"Button1": lazy.spawn(consts.rofi_app_cmd)},
        ),
        widget.Prompt(
            background=consts.colors("bg"),
        ),
        # widget.TextBox(
        #     fmt="Search",
        #     background=consts.colors("bg"),
        #     foreground=consts.colors("active"),
        #     mouse_callbacks={"Button1": lazy.spawn(consts.rofi_app_cmd)},
        # ),
        widget.Image(
            filename=consts.icons("sep4"),
        ),
        widget.WindowName(
            background=consts.colors("bg_alt"),
            format="{name}",
            foreground=consts.colors("active"),
            empty_group_string="Desktop",
        ),
        widget.Image(
            filename=consts.icons("sep3"),
        ),
        widget.Image(
            filename=consts.icons("download"),
            background=consts.colors("bg"),
        ),
        widget.Net(
            interface="wlan0",
            format="{down:.1f}{down_suffix}",
            background=consts.colors("bg"),
        ),
        widget.Image(
            filename=consts.icons("upload"),
            background=consts.colors("bg"),
        ),
        widget.Net(
            interface="wlan0",
            format="{up:.1f}{up_suffix}",
            background=consts.colors("bg"),
        ),
        widget.Spacer(
            length=3,
            background=consts.colors("bg"),
        ),
        widget.Systray(
            background=consts.colors("bg"),
            fontsize=20,
        ),
        widget.Image(
            filename=consts.icons("sep6"),
            background=consts.colors("bg_alt"),
        ),
        # widget.Image(
        #     filename=consts.icons("cpu"),
        #     background=consts.colors("bg_alt"),
        # ),
        # widget.CPUGraph(
        #     background=consts.colors("bg_alt"),
        #     border_color=consts.colors("bg"),
        #     fill_color=consts.colors("bg"),
        #     graph_color=consts.colors("active"),
        # ),
        # widget.CPU(
        #     background=consts.colors("bg_alt"),
        #     foreground=consts.colors("active"),
        # ),
        # widget.Image(
        #     filename=consts.icons("sep2"),
        # ),
        # widget.Spacer(
        #     length=8,
        #     background=consts.colors("bg_alt"),
        # ),
        # TODO: Work on custom spotify widget
        # spotify_widget(),
        widget.Image(
            filename=consts.icons("ram"),
            background=consts.colors("bg_alt"),
        ),
        widget.MemoryGraph(
            background=consts.colors("bg_alt"),
            border_color=consts.colors("bg"),
            fill_color=consts.colors("bg"),
            graph_color=consts.colors("active"),
        ),
        widget.Memory(
            background=consts.colors("bg_alt"),
            foreground=consts.colors("active"),
            format="{MemUsed: .0f}{mm}",
            update_interval=5,
        ),
        widget.Image(
            filename=consts.icons("sep2"),
        ),
        widget.Spacer(
            length=8,
            background=consts.colors("bg_alt"),
        ),
        widget.BatteryIcon(
            theme_path=consts.icons("battery_theme"),
            background=consts.colors("bg_alt"),
            scale=1,
        ),
        widget.Battery(
            background=consts.colors("bg_alt"),
            foreground=consts.colors("active"),
            format="{percent:2.0%}",
        ),
        widget.Image(
            filename=consts.icons("sep2"),
        ),
        widget.Spacer(
            length=8,
            background=consts.colors("bg_alt"),
        ),
        widget.PulseVolume(
            theme_path=consts.icons("volume_theme"),
            # emoji=True,
            background=consts.colors("bg_alt"),
        ),
        widget.Spacer(
            length=-5,
            background=consts.colors("bg_alt"),
        ),
        widget.PulseVolume(
            background=consts.colors("bg_alt"),
            foreground=consts.colors("active"),
        ),
        widget.Image(
            filename=consts.icons("sep5"),
            background=consts.colors("bg_alt"),
        ),
        widget.Image(
            filename=consts.icons("clock"),
            background=consts.colors("bg"),
            margin_y=6,
            margin_x=5,
        ),
        widget.Clock(
            format="%I:%M %p",
            background=consts.colors("bg"),
            foreground=consts.colors("active"),
        ),
        widget.Spacer(
            length=3,
            background=consts.colors("bg"),
        ),
        widget.Image(
            filename=consts.icons("today"),
            background=consts.colors("bg"),
            margin_y=6,
            margin_x=5,
        ),
        widget.Clock(
            format="%a, %d %b",
            background=consts.colors("bg"),
            foreground=consts.colors("active"),
        ),
        widget.Spacer(
            length=18,
            background=consts.colors("bg"),
        ),
    ],
    30,
    border_color=consts.colors("bg"),
    border_width=[0, 0, 0, 0],
    margin=[15, 9, 6, 9],
)

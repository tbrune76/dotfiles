# -*- coding: utf-8 -*-
# # Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess

from libqtile import bar, hook, layout, widget, qtile
from libqtile.config import EzClick as Click, EzDrag as Drag, Group, EzKey as Key, Match, ScratchPad, DropDown, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

try:
    from typing import List  # noqa: F401
except ImportError:
    pass


mod = "mod4"
terminal = guess_terminal()
myBrowser = "brave"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key("M-h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key("M-l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key("M-j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key("M-k",
        lazy.layout.up(),
        desc="Move focus up"),

    Key("M-S-h",
        lazy.layout.swap_left(),
        desc="Swap window left"),
    Key("M-S-l",
        lazy.layout.swap_right(),
        desc="Swap window right"),
    Key("M-S-j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key("M-S-k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    Key("M-C-j",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key("M-C-k",
        lazy.layout.grow(),
        desc="Grow window"),
    # Key("M-C-j", lazy.layout.shrink_main(), desc="Shrink main window"),
    # Key("M-C-k", lazy.layout.grow_main(), desc="Grow main window"),
    Key("M-C-h",
        lazy.layout.reset(),
        desc="Reset layout"),
    Key("M-C-l",
        lazy.layout.normalize(),
        desc="Normalize layout"),
    Key("M-C-m",
        lazy.layout.maximize(),
        desc="Maximize"),

    Key("M-S-<Return>",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),
    Key("<XF86AudioMute>",
        lazy.spawn("amixer -q set Master toggle"),
        desc="Toggle Mute"),
    Key("<XF86AudioLowerVolume>",
        lazy.spawn("amixer -q set Master 5%- unmute"),
        desc="Lower Volume"),
    Key("<XF86AudioRaiseVolume>",
        lazy.spawn("amixer -q set Master 5%+ unmute"),
        desc="Raise Volume"),
    Key("<XF86Calculator>",
        lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"),
        desc="Launch Calculator"),
    Key("<Print>",
        lazy.spawn("flameshot gui -d 3000"),
        desc="Take Screenshot"),
    Key("M-<Return>",
        lazy.spawn(terminal),
        desc="Launch terminal"),
    Key("M-<Tab>",
        lazy.next_layout(),
        desc="Toggle between layouts"),
    Key("M-q",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key("M-C-r",
        lazy.reload_config(),
        desc="Reload the config"),
    Key("M-A-S-C-q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key("M-x",
        lazy.spawn("rofi -show menu -modi 'menu:rofi-power-menu'"),
        desc="Launch Power-Menu"),
    # Key("M-r",       lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key("M-b",
        lazy.spawn(myBrowser),
        desc="Launch Browser"),
    Key("M-p",
        lazy.spawn("brave --incognito"),
        desc="Launch Private-Brave"),
    Key("M-d",
        lazy.spawn("udiskie-dmenu -matching regex -dmenu -i -no-custom -multi-select"),
        desc="Launch Drive-Menu"),
    Key("M-e",
        lazy.spawn("pcmanfm"),
        desc="Launch PCManFM"),
    Key("M-<Space>",
        lazy.spawn("rofi -show combi"),
        desc="Launch rofi"),
    Key("C-<odiaeresis>",
        lazy.spawn("clipmenu -i"),
        desc="Launch Clipboard"),
    Key("M-<adiaeresis>",
        lazy.spawn("rofi-rbw"),
        desc="Launch Bitwarden Type"),
]

#           ["#62e31a", "#62e31a"], # color 29 extra3
#           ["#19b6d6", "#19b6d6"], # color 30 arch blue


highlight_color = ["#62e31a", "#62e31a"]   # color 29 extra3
# highlight_color = ["#fe8019", "#fe8019"]
highlight_floating = ["#D01515", "#D01515"]
# Groups = [Group(i) for i in "123456789"]

# Colorschemes: Doom-One, Dracula, Nord, Gruvbox, Solarized
color_scheme = {
   "doom-one": [["#282c34", "#282c34"],  # colors[0] - Black (Background)
                ["#dfdfdf", "#dfdfdf"],  # colors[1] - White (Foreground)
                ["#46d9ff", "#46d9ff"],  # colors[2] - Cyan
                ["#51afef", "#51afef"],  # colors[3] - Blue
                ["#a9a1e1", "#a9a1e1"],  # colors[4] - Purple
                ["#c678dd", "#c678dd"],  # colors[5] - Pink
                ["#ff6c6b", "#ff6c6b"],  # colors[6] - Red
                ["#da8548", "#da8548"],  # colors[7] - Orange
                ["#ecbe7b", "#ecbe7b"],  # colors[8] - Yellow
                ["#98be65", "#98be65"],  # colors[9] - Green
                ["#3e4556", "#3e4556"],  # colors[10] - Separator / Border Normal
                ["#c678dd", "#c678dd"]], # colors[11] - Border Focus

    "dracula": [["#282a36", "#282a36"],  # colors[0] - Black (Background)
                ["#f8f8f2", "#f8f8f2"],  # colors[1] - White (Foreground)
                ["#8be9fd", "#8be9fd"],  # colors[2] - Cyan
                ["#6272a4", "#6272a4"],  # colors[3] - Blue
                ["#bd93f9", "#bd93f9"],  # colors[4] - Purple
                ["#ff79c6", "#ff79c6"],  # colors[5] - Pink
                ["#ff5555", "#ff5555"],  # colors[6] - Red
                ["#ffb86c", "#ffb86c"],  # colors[7] - Orange
                ["#f1fa8c", "#f1fa8c"],  # colors[8] - Yellow
                ["#50fa7b", "#50fa7b"],  # colors[9] - Green
                ["#44475a", "#44475a"],  # colors[10] - Separator / Border Normal
                ["#bd93f9", "#bd93f9"]], # colors[11] - Border Focus

       "nord": [["#2e3440", "#2e3440"],  # colors[0] - Black (Background)
                ["#e5e9f0", "#e5e9f0"],  # colors[1] - White (Foreground)
                ["#88c0d0", "#88c0d0"],  # colors[2] - Cyan
                ["#81a1c1", "#81a1c1"],  # colors[3] - Blue
                ["#b48ead", "#b48ead"],  # colors[4] - Purple
                ["#8fbcbb", "#8fbcbb"],  # colors[5] - Teal
                ["#bf616a", "#bf616a"],  # colors[6] - Red
                ["#d08770", "#d08770"],  # colors[7] - Orange
                ["#ebcb8b", "#ebcb8b"],  # colors[8] - Yellow
                ["#a3be8c", "#a3be8c"],  # colors[9] - Green
                ["#4c566a", "#4c566a"],  # colors[10] - Separator/ Border Normal
                ["#88c0d0", "#88c0d0"]], # colors[11] - Border Focus

    "gruvbox": [["#282828", "#282828"],  # colors[0] - Black (Background)
                ["#ebdbb2", "#ebdbb2"],  # colors[1] - White (Foreground)
                ["#689d6a", "#689d6a"],  # colors[2] - Cyan
                ["#458588", "#458588"],  # colors[3] - Blue
                ["#b16286", "#b16286"],  # colors[4] - Purple
                ["#a89984", "#a89984"],  # colors[5] - Gray
                ["#cc241d", "#cc241d"],  # colors[6] - Red
                ["#d65d0e", "#d65d0e"],  # colors[7] - Orange
                ["#d79921", "#d79921"],  # colors[8] - Yellow
                ["#98971a", "#98971a"],  # colors[9] - Green
                ["#504945", "#504945"],  # colors[10] - Separator / Border Normal
                ["#a89984", "#a89984"]], # colors[11] - Border Focus

  "solarized": [["#002b36", "#002b36"],  # colors[0] - Black (Background)
                ["#fdf6e3", "#fdf6e3"],  # colors[1] - White (Foreground)
                ["#2aa198", "#2aa198"],  # colors[2] - Cyan
                ["#268bd2", "#268bd2"],  # colors[3] - Blue
                ["#6c71c4", "#6c71c4"],  # colors[4] - Purple
                ["#d33682", "#d33682"],  # colors[5] - Pink
                ["#dc322f", "#dc322f"],  # colors[6] - Red
                ["#cb4b16", "#cb4b16"],  # colors[7] - Orange
                ["#b58900", "#b58900"],  # colors[8] - Yellow
                ["#859900", "#859900"],  # colors[9] - Green
                ["#586e75", "#586e75"],  # colors[10] - Separator / Border Normal
                ["#2aa198", "#2aa198"]], # colors[11] - Border Focus
}

# Choose the colorscheme here:
colors = color_scheme["gruvbox"]

groups = [
    Group("1", layout="monadtall"),
    Group("2", layout="monadtall"),
    Group("3", layout="monadtall"),
    Group("4", layout="monadtall"),
    Group("5", layout="monadtall"),
    Group("6", layout="monadtall"),
    Group("7", layout="monadtall"),
    Group("8", layout="monadtall"),
    Group("9", layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key("M-" + i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
                ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key("M-S-" + i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
                ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term',
             terminal,
             width=0.5,
             height=0.6,
             x=0.25,
             y=0.15,
             opacity=1),
    DropDown('ranger',
             terminal + ' -e ranger',
             width=0.6,
             height=0.7,
             x=0.2,
             y=0.1,
             opacity=1),
    DropDown('mixer',
             terminal + ' -e pulsemixer',
             width=0.33,
             height=0.2,
             x=0.33,
             y=0.3,
             opacity=1),
]))

# extend keys list with keybinding for scratchpad
keys.extend([
    Key("C-1",
        lazy.group['scratchpad'].dropdown_toggle('term')),
    Key("C-2",
        lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key("M-<F10>",
        lazy.group['scratchpad'].dropdown_toggle('mixer')),
])

layout_theme = {
    "margin": 3,
    "border_width": 2,
    "border_focus": highlight_color,
    "border_normal": colors[10],
}

floating_theme = {
    "margin": 3,
    "border_width": 3,
    "border_focus": highlight_floating,
    "border_normal": colors[10],
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="Hurmit Nerd Font Mono SemiBold",
    # font="mononoki Nerd Font Mono SemiBold",
    # font="Hack Nerd Font Mono",
    # font="FuraMono Nerd Font Mono",
    font="BlexMono Nerd Font Mono SemiBold",
    fontsize=12,
    padding=5,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.WindowCount(
                #     show_zero=True,
                #     max_chars=2,
                # ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[2],
                    padding=1,
                    scale=0.75,
                ),
                # widget.CurrentLayout(
                #    foreground=colors[2],
                #    background=colors[0],
                #    padding=5,
                # ),
                widget.GroupBox(
                    padding=1,
                    font='BlexMono Nerd Font Mono',
                    highlight_method='line',
                    borderwidth=2,
                    this_current_screen_border=highlight_color,
                ),
                # widget.Prompt(
                # ),
                widget.TaskList(
                    font='BlexMono Nerd Font Mono',
                    icon_size=0,
                    border=highlight_color,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(
                ),
                # widget.StatusNotifier(
                # ),
                widget.Net(
                    interface="all",
                    format=' {down} ↑↓ {up}',
                    foreground=colors[9],
                    decorations=[
                        BorderDecoration(
                            colour=colors[9],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Volume(
                    fmt=' {}',
                    foreground=colors[3],
                    decorations=[
                        BorderDecoration(
                            colour=colors[3],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                # widget.Battery(
                #    foreground=colors[5],
                #    charge_char='',
                #    discharge_char='v',
                #    empty_char='',
                #    full_char='',
                #    unknown_char='?',
                #    format='{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f}W',
                #    padding=5,
                #    update_interval=60,
                # ),
                widget.Memory(
                    foreground=colors[5],
                    format=' {MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}',
                    measure_mem="G",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    decorations=[
                        BorderDecoration(
                            colour=colors[5],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.CPU(
                    foreground=colors[7],
                    format=' {load_percent}%',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    decorations=[
                        BorderDecoration(
                            colour=colors[7],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.ThermalSensor(
                    threshold=90,
                    format=' {temp:.1f}{unit}',
                    foreground=colors[8],
                    decorations=[
                        BorderDecoration(
                            colour=colors[8],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                widget.CheckUpdates(
                    distro="Arch_yay",
                    display_format=" {updates}",
                    colour_no_updates=colors[4],
                    colour_have_updates=colors[6],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Suy')},
                    decorations=[
                        BorderDecoration(
                            colour=colors[6],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Clock(
                    format="%a %d.%m.%Y (%W)",
                    foreground=colors[3],
                    update_interval=3600,
                    decorations=[
                        BorderDecoration(
                            colour=colors[3],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Clock(
                    format="%H:%M:%S",
                    foreground=colors[7],
                    decorations=[
                        BorderDecoration(
                            colour=colors[7],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **floating_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pinentry-gtk-2"),
        # Match(wm_class="pcmanfm"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

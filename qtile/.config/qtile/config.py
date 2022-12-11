# Copyright (c) 2010 Aldo Cortesi
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

import os, re, socket, subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import EzClick as Click, EzDrag as Drag, Group, EzKey as Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

try:
    from typing import List # noqa: F401
except ImportError:
    pass


mod = "mod4"
terminal = guess_terminal()
myBrowser = "brave"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key("M-h", lazy.layout.left(), desc="Move focus to left"),
    Key("M-l", lazy.layout.right(), desc="Move focus to right"),
    Key("M-j", lazy.layout.down(), desc="Move focus down"),
    Key("M-k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key("M-S-h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key("M-S-l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key("M-S-j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key("M-S-k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key("M-C-h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key("M-C-l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key("M-C-j", lazy.layout.grow_down(), desc="Grow window down"),
    Key("M-C-k", lazy.layout.grow_up(), desc="Grow window up"),
    Key("M-n",   lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key("M-S-<Return>",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key("<XF86AudioMute>", lazy.spawn("amixer -q set Master toggle")),
    Key("<XF86AudioLowerVolume>", lazy.spawn("amixer -q set Master 5%- unmute")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("amixer -q set Master 5%+ unmute")),
    Key("M-<F10>", lazy.spawn(terminal + " -e pulsemixer"), desc="Launch Pulsemixer"),
    Key("<XF86Calculator>", lazy.spawn("rofi -show -calc -modi calc -no-show-match -no-sort"), desc="Launch Calculator"),
    Key("M-<Return>", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key("M-<Tab>",   lazy.next_layout(), desc="Toggle between layouts"),
    Key("M-q",       lazy.window.kill(), desc="Kill focused window"),
    Key("M-C-r",     lazy.reload_config(), desc="Reload the config"),
    Key("M-C-S-A-q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key("M-r",       lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key("M-b",       lazy.spawn(myBrowser), desc="Launch Browser"),
    Key("M-p",       lazy.spawn("brave --incognito"), desc="Launch Private-Brave"),
    Key("M-e",       lazy.spawn("pcmanfm"), desc="Launch PCManFM"),
    Key("M-<Space>", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key("C-<odiaeresis>",       lazy.spawn("clipmenu -i"), desc="Launch Clipboard"),
    Key("M-<adiaeresis>",       lazy.spawn("rofi-rbw"), desc="Launch Bitwarden Type"),
]

colors = [["#282c34", "#282c34"], # color 0
          ["#1c1f24", "#1c1f24"], # color 1
          ["#dfdfdf", "#dfdfdf"], # color 2
          ["#ff6c6b", "#ff6c6b"], # color 3
          ["#98be65", "#98be65"], # color 4
          ["#da8548", "#da8548"], # color 5
          ["#51afef", "#51afef"], # color 6
          ["#c678dd", "#c678dd"], # color 7
          ["#46d9ff", "#46d9ff"], # color 8
          ["#a9a1e1", "#a9a1e1"], # color 9
          ["#70c0b1", "#70c0b1"], # color 10
          ["#2e3440", "#2e3440"], # color 11  dark grayish blue
          ["#2e3440", "#2e3440"], # color 12  dark grayish blue
          ["#3b4252", "#3b4252"], # color 13  very dark grayish blue
          ["#434c5e", "#434c5e"], # color 14  very dark grayish blue
          ["#4c566a", "#4c566a"], # color 15  very dark grayish blue
          ["#d8dee9", "#d8dee9"], # color 16  grayish blue
          ["#e5e9f0", "#e5e9f0"], # color 17  light grayish blue
          ["#eceff4", "#eceff4"], # color 18  light grayish blue
          ["#8fbcbb", "#8fbcbb"], # color 19  grayish cyan
          ["#88c0d0", "#88c0d0"], # color 20  desaturated cyan
          ["#81a1c1", "#81a1c1"], # color 21 desaturated blue
          ["#5e81ac", "#5e81ac"], # color 22 dark moderate blue
          ["#bf616a", "#bf616a"], # color 23 slightly desaturated red
          ["#d08770", "#d08770"], # color 24 desaturated red
          ["#ebcb8b", "#ebcb8b"], # color 25 soft orange
          ["#a3be8c", "#a3be8c"], # color 26 desaturated green
          ["#b48ead", "#b48ead"], # color 27 grayish magenta
          ["#D01515", "#D01515"], # color 28
          ["#62e31a", "#62e31a"], # color 29 extra3:q
          ["#19b6d6", "#19b6d6"], # color 30 arch blue
         ]

#Groups = [Group(i) for i in "123456789"]

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


layout_theme = {
    "margin": 3,
    "border_width": 2,
    "border_focus": colors[29],
    "border_normal": "#606060",
}

floating_theme = {
    "margin": 3,
    "border_width": 4,
    "border_focus": colors[28],
    "border_normal": "#606060",
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="BlexMono Nerd Font Mono SemiBold",
    fontsize=11,
    padding=5,
    background = colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.WindowCount(
                    show_zero = True,
                    max_chars = 2,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground = colors[2],
                    padding = 1,
                    scale = 0.75,
                ),
                #widget.Image(
                #    filename = '~/.config/qtile/icons/python.png',
                #    scale = "False",
                #    mouse_callbacks={"Button1": lambda : qtile.cmd_spawn('rofi -show drun')},
                #),
                #widget.CurrentLayout(
                #    foreground = colors[2],
                #    background = colors[0],
                #    padding = 5,
                #),
                widget.GroupBox(
                    foreground = colors[2],
                    padding = 1,
                    font = 'BlexMono Nerd Font Mono',
                    highlight_method = 'line',
                    borderwidth = 2,
                    this_current_screen_border = colors[29],
                    urgent_alert_method = 'line',
                    urgent_border = colors[28],

                ),
                #widget.Prompt(
                #),
                #widget.WindowName(
                #    font = "BlexMono Nerd Font Mono",
                #),
                #widget.WindowTabs(),
                widget.TaskList(
                    font = 'BlexMono Nerd Font Mono',
                    icon_size = 0,
                    #highlight_method = 'block',
                    border = colors[29],
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(
                ),
                #widget.StatusNotifier(
                #),
                widget.Net(
                    interface = "all",
                    format = '↓ {down} ↑ {up}',
                    foreground = colors[3],
                ),
                widget.Volume(
                    fmt = 'Vol: {}',
                    foreground = colors[7],
                ),
                widget.CheckUpdates(
                    distro = "Arch_yay",
                    display_format = "U: ({updates})",
                    colour_no_updates = colors[4],
                    colour_have_updates = colors[3],
                ),
                widget.Memory(
                    foreground = colors[5],
                    format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                ),
                widget.CPU(
                    foreground = colors[9],
                    format = 'CPU: {load_percent}%',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                ),
                widget.ThermalSensor(
                    threshold = 90,
                    #fmt = 'Temp: {}',
                    foreground = colors[4],
                ),
                # widget.Battery(
                #    foreground = colors[5],
                #    charge_char = '^',
                #    discharge_char = 'v',
                #    empty_char = 'x',
                #    full_char = '=',
                #    unknown_char = '?',
                #    format = '{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f}W',
                #    padding = 5,
                #    update_interval = 60,
                #),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(
                    format="%a %d.%m.%Y (%W)",
                    foreground = colors[6],
                ),
                widget.Clock(
                    format="%H:%M:%S",
                    foreground = colors[25],
                ),
                # widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        #wallpaper = '/usr/share/backgrounds/arch-logo-dark/ALDark1.png',
        #wallpaper_mode = 'none',
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
        #Match(wm_class="pcmanfm"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.restart
def cleanup():
    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))

#@hook.subscribe.shutdown
#def killall():
#    shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))
#    subprocess.Popen(['killall', 'urxvtd', 'lxpolkit', 'nitrogen', 'picom'])
#
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

#@hook.subscribe.startup
#def start_always():
#    # Set the cursor to something sane in X
#    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


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

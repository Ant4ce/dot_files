#!/bin/env python 
import re
from xkeysnail.transform import *

# multipurpose mappings
define_multipurpose_modmap(
    # casplock acts as Escape when pressed and released
    # and as Control when held down with another key
    {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]},
)
define_keymap(None, {
    # AltGr + hjkl acts as arrow keys
    K("LM-h"): K("left"),
    K("LM-j"): K("down"),
    K("LM-k"): K("up"),
    K("LM-l"): K("right"),
    # alt works as expected
    K("LM-RM-h"): K("LM-left"),
    K("LM-RM-j"): K("LM-down"),
    K("LM-RM-k"): K("LM-up"),
    K("LM-RM-l"): K("LM-right"),
    # ctrl works as expected
    K("C-LM-h"): K("C-left"),
    K("C-LM-j"): K("C-down"),
    K("C-LM-k"): K("C-up"),
    K("C-LM-l"): K("C-right"),
    # shift works as expecteed
    K("Shift-LM-h"): K("Shift-left"),
    K("Shift-LM-j"): K("Shift-down"),
    K("Shift-LM-k"): K("Shift-up"),
    K("Shift-LM-l"): K("Shift-right"),

    # ctrl + shift works as expecteed
    K("C-Shift-LM-h"): K("C-Shift-left"),
    K("C-Shift-LM-j"): K("C-Shift-down"),
    K("C-Shift-LM-k"): K("C-Shift-up"),
    K("C-Shift-LM-l"): K("C-Shift-right"),
    # alt + shift works as expecteed
    K("LM-Shift-RM-h"): K("LM-Shift-left"),
    K("LM-Shift-RM-j"): K("LM-Shift-down"),
    K("LM-Shift-RM-k"): K("LM-Shift-up"),
    K("LM-Shift-RM-l"): K("LM-Shift-right"),
    # ctrl + alt works as expected
    K("C-LM-RM-h"): K("C-LM-left"),
    K("C-LM-RM-j"): K("C-LM-down"),
    K("C-LM-RM-k"): K("C-LM-up"),
    K("C-LM-RM-l"): K("C-LM-right"),

    # ctrl + shift + alt works as expected
    K("C-Shift-LM-RM-h"): K("C-Shift-LM-left"),
    K("C-Shift-LM-RM-j"): K("C-Shift-LM-down"),
    K("C-Shift-LM-RM-k"): K("C-Shift-LM-up"),
    K("C-Shift-LM-RM-l"): K("C-Shift-LM-right"),

    # disable arrow keys for evarrr
    K("left"):  K("UNKNOWN"),
    K("down"):  K("UNKNOWN"),
    K("up"):    K("UNKNOWN"),
    K("right"): K("UNKNOWN"),

    # disable enter
    #K("enter"): K("UNKNOWN"),

    # disable backspace
    #K("backspace"): K("UNKNOWN"),

}, "hjkl arrow keys")


# Keybindings for chosen apps 
define_keymap(re.compile("firefox|discord|TelegramDesktop|Slack"), {
    # use ctrl+u/d to page up/down
    K("C-u"): K("page_up"),
    K("C-d"): K("page_down"),
}, "Discord, Slack, Signal, Riot, Jitsi Meet and Telegram")
#works in all places 

define_keymap(None, {
    # ctrl+m works as enter
    K("C-m"): K("enter"),
    # ctrl+h works as backspace
    K("C-h"): K("backspace"),
}, "Enable readline outside of applications that already have them")

define_keymap(lambda wm_class: wm_class not in ("Gnome-terminal"), {
    # ctrl+j deletes a word
    K("C-j"): K("C-backspace"),
}, "")

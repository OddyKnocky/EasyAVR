# Easy AVR USB Keyboard Firmware Keymapper
# Copyright (C) 2013-2016 David Howland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Keyboard definition for the Smallfry custom keyboard."""

import easykeymap.templates.ATmega32U4_16MHz_SIXTY as firmware
from easykeymap.ioports import *

description = "JD40"
unique_id = "SMALLFRY_001"
cfg_name = "smallfry"

teensy = True
hw_boot_key = False

display_height = int(4*4)
display_width = int(12*4)

num_rows = 4
num_cols = 12

strobe_cols = False
strobe_low = True

matrix_hardware = [
#     Port mask     Dir mask
    ( 0b01101111 , 0b00000000 ),    # REF_PORTB
    ( 0b00000000 , 0b00000000 ),    # REF_PORTC
    ( 0b00001111 , 0b00001111 ),    # REF_PORTD
    ( 0b00000000 , 0b00000000 ),    # REF_PORTE
    ( 0b11110011 , 0b00000000 )     # REF_PORTF
]

matrix_strobe = [
#     REF_PORTB    REF_PORTC    REF_PORTD    REF_PORTE    REF_PORTF
    ( 0b00000000 , 0b00000000 , 0b00001110 , 0b00000000 , 0b00000000 ),
    ( 0b00000000 , 0b00000000 , 0b00001101 , 0b00000000 , 0b00000000 ),
    ( 0b00000000 , 0b00000000 , 0b00001011 , 0b00000000 , 0b00000000 ),
    ( 0b00000000 , 0b00000000 , 0b00000111 , 0b00000000 , 0b00000000 )
]

matrix_sense = [
#      Port        Pin mask
    ( REF_PORTF , (1 << 0) ),
    ( REF_PORTF , (1 << 1) ),
    ( REF_PORTF , (1 << 4) ),
    ( REF_PORTF , (1 << 5) ),
    ( REF_PORTF , (1 << 6) ),
    ( REF_PORTF , (1 << 7) ),
    ( REF_PORTB , (1 << 0) ),
    ( REF_PORTB , (1 << 1) ),
    ( REF_PORTB , (1 << 2) ),
    ( REF_PORTB , (1 << 3) ),
    ( REF_PORTB , (1 << 5) ),
    ( REF_PORTB , (1 << 6) )
]

num_leds = 1
num_ind = 1
num_bl_enab = 2

led_definition = [
    ('Caps Key', 'Caps Lock')
]

led_hardware = [
#       Port    Pin    Direction
    ( REF_PORTD, 7, LED_DRIVER_PULLUP )
]

backlighting = False

bl_modes = [
    ( 0 ),
    ( 1 )
]

KMAC_key = None

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_ESCAPE'),
     ((4, 4), (0, 1), 'HID_KEYBOARD_SC_Q'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_W'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (0, 4), 'HID_KEYBOARD_SC_R'),
     ((4, 4), (0, 5), 'HID_KEYBOARD_SC_T'),
     ((4, 4), (0, 6), 'HID_KEYBOARD_SC_Y'),
     ((4, 4), (0, 7), 'HID_KEYBOARD_SC_U'),
     ((4, 4), (0, 8), 'HID_KEYBOARD_SC_I'),
     ((4, 4), (0, 9), 'HID_KEYBOARD_SC_O'),
     ((4, 4), (0, 10), 'HID_KEYBOARD_SC_P'),
     ((4, 4), (0, 11), 'HID_KEYBOARD_SC_BACKSPACE')],

    [((5, 4), (1, 0), 'HID_KEYBOARD_SC_TAB'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_A'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_S'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_D'),
     ((4, 4), (1, 4), 'HID_KEYBOARD_SC_F'),
     ((4, 4), (1, 5), 'HID_KEYBOARD_SC_G'),
     ((4, 4), (1, 6), 'HID_KEYBOARD_SC_H'),
     ((4, 4), (1, 7), 'HID_KEYBOARD_SC_J'),
     ((4, 4), (1, 8), 'HID_KEYBOARD_SC_K'),
     ((4, 4), (1, 9), 'HID_KEYBOARD_SC_L'),
     ((7, 4), (1, 10), 'HID_KEYBOARD_SC_ENTER')],

    [((7, 4), (2, 0), 'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), (2, 1), 'HID_KEYBOARD_SC_Z'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_X'),
     ((4, 4), (2, 3), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (2, 4), 'HID_KEYBOARD_SC_V'),
     ((4, 4), (2, 5), 'HID_KEYBOARD_SC_B'),
     ((4, 4), (2, 6), 'HID_KEYBOARD_SC_N'),
     ((4, 4), (2, 7), 'HID_KEYBOARD_SC_M'),
     ((4, 4), (2, 8), 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((5, 4), (2, 9), 'HID_KEYBOARD_SC_RIGHT_SHIFT'),
     ((4, 4), (2, 10), 'SCANCODE_FN')],

    [((5, 4), (3, 0), 'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((4, 4), (3, 1), 'HID_KEYBOARD_SC_DELETE'),
     ((4, 4), (3, 2), 'HID_KEYBOARD_SC_LEFT_ALT'),
     ((25, 4), (3, 5), 'HID_KEYBOARD_SC_SPACE'),
     ((5, 4), (3, 9), 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((5, 4), (3, 10), 'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK')]
]

alt_layouts = {}

#!/usr/bin/env python

import os
from shutil import copyfile

GAME_ID = '211820'

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

STEAMAPPS_PATH = os.path.dirname(os.path.dirname(GAME_PATH))

WORKSHOP_PATH = os.path.join(STEAMAPPS_PATH, 'workshop', 'content', GAME_ID)

MODS_PATH = os.path.join(GAME_PATH, 'mods')


def make_links():
    for directory, sub_dirs, files in os.walk(WORKSHOP_PATH):
        for file in files:
            if '.pak' in file:
                new_file_name = '{}.pak'.format(os.path.basename(directory))
                server_mod_path = os.path.join(MODS_PATH, new_file_name)
                mod_path = os.path.join(directory, file)
                print("{}->{}".format(mod_path, server_mod_path))
                copyfile(mod_path, server_mod_path)


if __name__ == '__main__':
    print("GAME_PATH: {}".format(GAME_PATH))
    print("STEAMAPPS_PATH: {}".format(STEAMAPPS_PATH))
    print("WORKSHOP_PATH: {}".format(WORKSHOP_PATH))
    print("MODS_PATH: {}".format(MODS_PATH))
    make_links()

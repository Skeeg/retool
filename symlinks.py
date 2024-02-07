import os
import json
import re

def create_symlink(main_entry_name, game_info):
    actualFileName = game_info['name']
    symlinkName = re.sub(r'\.nes$', '.zip', actualFileName)
    symlinkTarget = main_entry_name + '.zip'
    os.symlink(symlinkName, symlinkTarget)
    print(f"Created symlink: {symlinkName} to {symlinkTarget}")

def process_link(json_data):
    for game_entry in json_data:
        main_entry_name = list(game_entry.keys())[0]
        game_info_list = game_entry[main_entry_name]

        for game_info in game_info_list:
            try:
                create_symlink(main_entry_name, game_info)
            except Exception as e:
                print(f"Error creating symlink for {main_entry_name}: {e}")
                print(f"Game Info: {game_info}")
            

if __name__ == "__main__":
    # Load JSON data from a file
    map_file = os.environ.get('MAP_FILE')
    output_directory = os.environ.get('OUTPUT_DIR')
    rom_relative_path = os.environ.get('ROM_RELATIVE_PATH')
    media_relative_path = os.environ.get('MEDIA_RELATIVE_PATH')
    with open(map_file, 'r') as json_file:
        map_data = json.load(json_file)

    #Need to build the map json file
    # Things to do:
        # point to the 1g1r json outputs
        # supply the roms path (no-intro/redump)
        # supply the unique media path name
        # supply the frontend file structure
            # emudeck = roms/NES & ../downloaded_media/NES for media
            # onionOS = roms/FC & roms/FC/img for media
            # etc.
        # supply the media file structure
    print(f"Map File: {map_file}")

    # process_link(json_data)

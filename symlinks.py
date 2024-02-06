import os
import json
import re

def create_symlink(main_entry_name, game_info):
    actualFileName = game_info['name']
    symlinkName = re.sub(r'\.nes$', '.zip', actualFileName)
    symlinkTarget = main_entry_name + '.zip'
    os.symlink(symlinkName, symlinkTarget)
    print(f"Created symlink: {symlinkName} to {symlinkTarget}")

def process_json(json_data):
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
    input_file_path = os.environ.get('INPUT_FILE')
    with open(input_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    process_json(json_data)
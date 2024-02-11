import os
import json
import re
from glob import glob

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

def get_symlink_files(directory):
    symlink_files = []
    directory_listing = os.listdir(directory)
    for filename in directory_listing:
        if filename.endswith(".symlinkdata.json"):
            symlink_files.append(filename)
    return symlink_files

def trim_to_single_trailing_slash(input_string):
    return input_string.rstrip("/") + "/"

# def extract_datfiles(data):
#     datfiles = []
#     systems = data.get('Systems', {})
#     for system_info in systems.values():
#         datfile = system_info.get('datfile')
#         if datfile:
#             datfiles.append(datfile)
#     return datfiles

# def match_filenames(truncated_strings, full_filenames):
#     matched_filenames = []

#     for string in truncated_strings:
#         for filename in full_filenames:
#             if filename.startswith(string + ' ('):
#                 matched_filenames.append((string, filename))
#                 break  # Break once a match is found to avoid unnecessary iterations

    # return matched_filenames

def match_dat_filename(truncated_string, full_filenames):
    for filename in full_filenames:
        if filename.startswith(truncated_string + ' ('):
            return filename
    
    return None

def find_files_with_string(base_path, search_string):
    result = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if search_string in file:
                result.append(os.path.join(root, file))
    return result

def walk_directory(base_path):
    result = {}
    for root, dirs, files in os.walk(base_path):
        for directory in dirs:
            directory_path = os.path.join(root, directory)
            relative_path = os.path.relpath(directory_path, base_path)
            result[relative_path] = []
            for file in os.listdir(directory_path):
                result[relative_path].append(file)
    return result

if __name__ == "__main__":
    # Establish Variables
    map_file = os.environ.get('MAP_FILE')
    base_1g1r_directory = os.environ.get('BASE_1G1R_DIRECTORY')
    base_media_directory = os.environ.get('BASE_MEDIA_DIRECTORY')
    dats_subdirectory = os.environ.get('DATS_SUBDIRECTORY')
    links_subdirectory = os.environ.get('LINKS_SUBDIRECTORY')
    rom_vault_relative_path = os.environ.get('ROM_VAULT_RELATIVE_PATH')
    media_vault_relative_path = os.environ.get('MEDIA_VAULT_RELATIVE_PATH')

    # Load the map file
    with open(map_file, 'r') as json_file:
        map_data = json.load(json_file)
        
    all_symlink_files = get_symlink_files(base_1g1r_directory + dats_subdirectory)
    
    for system in map_data['Systems']:
        full_system = map_data['Systems'][system]
        symlink_file = match_dat_filename(map_data['Systems'][system]['datfile'], all_symlink_files)
        screenscraper_subfolder = map_data['Systems'][system]['screenscraper_folder']
        screenscraper_folder = base_media_directory + screenscraper_subfolder
        media_files = walk_directory(screenscraper_folder)
        if symlink_file:
            with open(base_1g1r_directory + dats_subdirectory + symlink_file, 'r') as json_file:
                game_data = json.load(json_file)
            for game in game_data:
                game_name = list(game.keys())[0]
                for file in game[game_name]:
                    file_data = os.path.splitext(file['name'])
                    if not file_data[1] in full_system['ignore_extensions']:
                        rom_name = {}
                        rom_name['full'] = file_data[0]
                        rom_name['short'] = game_name
                        for frontend in full_system['frontends']:
                            rom_name_preference = map_data['frontends'][frontend]['rom_name_preference']
                            rom_vault_relative_path = os.environ.get('ROM_VAULT_RELATIVE_PATH')
                            rom_vault_relative_path = rom_vault_relative_path + full_system['datsource'] + '/' + full_system['datfile'] + '/'
                            frontend_folder = base_1g1r_directory + links_subdirectory + frontend
                            frontend_roms_folder = frontend_folder + full_system['frontends'][frontend]['roms_path']
                            frontend_linked_file_path = frontend_roms_folder + rom_name[rom_name_preference] + full_system['linked_extension']
                            frontend_roms_path_depth = full_system['frontends'][frontend]['roms_path'].count('/')
                            for i in range(frontend_roms_path_depth):
                                rom_vault_relative_path = "../" + rom_vault_relative_path
                            actual_file_relative_path = rom_vault_relative_path + rom_name['full'] + full_system['linked_extension']
                            try:
                                os.makedirs(frontend_roms_folder, exist_ok=True)
                                os.symlink(src=actual_file_relative_path, dst=frontend_linked_file_path)
                                print(f"Created symlink: {actual_file_relative_path} to {frontend_linked_file_path}")
                            except FileExistsError:
                                print(f"Link already exists: {frontend_linked_file_path}")
                            except Exception as e:
                                print(f"Error creating symlink for {game_name}: {e}")
                                print(f"Game Info: {file}")
                            
                            frontend_media_paths = map_data['frontends'][frontend]['media_paths']
                            for media_path in frontend_media_paths:
                                #Define Paths
                                actual_media_asset_path = frontend_media_paths[media_path]
                                frontend_asset_path = media_path
                                frontend_media_folder = frontend_folder + full_system['frontends'][frontend]['media_path'] + frontend_asset_path
                                media_vault_relative_path = os.environ.get('MEDIA_VAULT_RELATIVE_PATH')
                                media_vault_relative_path = media_vault_relative_path + screenscraper_subfolder + '/' + actual_media_asset_path + '/'
                                frontend_media_path_depth = full_system['frontends'][frontend]['media_path'].count('/')
                                for i in (range(frontend_media_path_depth + 1)):
                                    media_vault_relative_path = "../" + media_vault_relative_path
                                #First find matches in the folder
                                matched_media_files = []
                                for media_file in media_files[actual_media_asset_path]:
                                    if rom_name['full'] in media_file:
                                        matched_media_files.append(media_file)
                                # print(matched_media_files)
                                mapped_media_filenames = []
                                for matched_filenames in matched_media_files:
                                    mapped_media_extension = os.path.splitext(matched_filenames)[1]
                                    mapped_media_filenames.append({'preffered_name': rom_name[rom_name_preference] + mapped_media_extension, 'actual_name': rom_name['full'] + mapped_media_extension})
                                # print(mapped_media_filenames)
                                #Then create the symlink
                                # frontend_media_file_path = frontend_media_folder + rom_name[rom_name_preference] + full_system['frontends'][frontend]['media_path']
                                for item in mapped_media_filenames:
                                    actual_media_file_relative_path = os.path.join(media_vault_relative_path, item['actual_name'])
                                    frontend_linked_media_file_path = os.path.join(frontend_media_folder, item['preffered_name'])
                                    try:
                                        os.makedirs(frontend_media_folder, exist_ok=True)
                                        os.symlink(src=actual_media_file_relative_path, dst=frontend_linked_media_file_path)
                                        print(f"Created symlink: {actual_media_file_relative_path} to {frontend_linked_media_file_path}")
                                    except FileExistsError:
                                        print(f"Link already exists: {frontend_linked_media_file_path}")
                                    except Exception as e:
                                        print(f"Error creating symlink for {game_name}: {e}")
                                        print(f"Game Info: {file}")
                                    
                                # for i in range(frontend_media_path_depth):
                                #     media_vault_relative_path = "../" + media_vault_relative_path
                                # actual_media_relative_path = media_vault_relative_path + rom_name['full'] + full_system['frontends'][frontend]['media'][media]['media_extension']
                                # try:
                                #     os.makedirs(frontend_media_folder, exist_ok=True)
                                #     os.symlink(src=actual_media_relative_path, dst=frontend_media_file_path)
                                # except FileExistsError:
                                #     print(f"File already exists: {frontend_media_file_path}")
                                # except Exception as e:
                                #     print(f"Error creating symlink for {game_name}: {e}")
                                #     print(f"Game Info: {file}")
                                # finally:
                                #     print(f"Created symlink: {actual_media_relative_path} to {frontend_media_file_path}")
                            
                        
                # try:
                #     create_symlink(system, game_info)
                # except Exception as e:
                #     print(f"Error creating symlink for {system}: {e}")
                #     print(f"Game Info: {game_info}")
            
        else:
            print(f"Symlink file not found: {symlink_file}")

    # print(json.dumps(all_symlink_files, indent=2, sort_keys=True))

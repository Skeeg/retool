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

def get_symlink_files(directory):
    symlink_files = []
    directory_listing = os.listdir(directory)
    for filename in directory_listing:
        if filename.endswith(".symlinkdata.json"):
            symlink_files.append(filename)
    return symlink_files

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

if __name__ == "__main__":
    # Establish Variables
    map_file = os.environ.get('MAP_FILE')
    base_1g1r_directory = os.environ.get('BASE_1G1R_DIRECTORY')
    dats_subdirectory = os.environ.get('DATS_SUBDIRECTORY')
    links_subdirectory = os.environ.get('LINKS_SUBDIRECTORY')
    rom_vault_relative_path = os.environ.get('ROM_VAULT_RELATIVE_PATH')
    media_vault_relative_path = os.environ.get('MEDIA_VAULT_RELATIVE_PATH')

    # Load the map file
    with open(map_file, 'r') as json_file:
        map_data = json.load(json_file)
        
    all_symlink_files = get_symlink_files(base_1g1r_directory + dats_subdirectory)
    # datfiles_to_process = extract_datfiles(map_data)
    # mapping_data = extract_datfiles(map_data)

    # for datfile in datfiles_to_process:
    #     symlink_file = datfile + ".symlinkdata.json"
    #     if symlink_file in all_symlink_files:
    #         with open(base_1g1r_directory + dats_subdirectory + symlink_file, 'r') as json_file:
    #             json_data = json.load(json_file)
    #             process_link(json_data)
    #     else:
    #         print(f"Symlink file not found: {symlink_file}")

    # actual_files_to_process = match_filenames(sorted(datfiles_to_process), sorted(all_symlink_files, reverse=True))
    # print(actual_files_to_process)

    # for record in actual_files_to_process:
    #     system = record[0]
    #     symlink_file = record[1]
    #     with open(base_1g1r_directory + dats_subdirectory + symlink_file, 'r') as json_file:
    #         json_data = json.load(json_file)
    #         process_link(json_data)
    for system in map_data['Systems']:
        full_system = map_data['Systems'][system]
        symlink_file = match_dat_filename(map_data['Systems'][system]['datfile'], all_symlink_files)
        if symlink_file:
            with open(base_1g1r_directory + dats_subdirectory + symlink_file, 'r') as json_file:
                game_data = json.load(json_file)
            for game in game_data:
                game_name = list(game.keys())[0]
                for file in game[game_name]:
                    file_data = os.path.splitext(file['name'])
                    if not file_data[1] in full_system['ignore_extensions']:
                        rom_name = file_data[0] + full_system['linked_extension']
                        if full_system['use_rom_file_name'] == "True":
                            link_name = file_data[0] + full_system['linked_extension']
                        else:
                            link_name = game_name + full_system['linked_extension']

                        for frontend in full_system['frontends']:
                            rom_vault_relative_path = os.environ.get('ROM_VAULT_RELATIVE_PATH')
                            rom_vault_relative_path = rom_vault_relative_path + full_system['datsource'] + '/' + full_system['datfile'] + '/'
                            frontend_folder = base_1g1r_directory + links_subdirectory + frontend
                            frontend_roms_folder = frontend_folder + full_system['frontends'][frontend]['roms_path']
                            frontent_linked_file_path = frontend_roms_folder + link_name
                            front_end_roms_path_depth = full_system['frontends'][frontend]['roms_path'].count('/')
                            for i in range(front_end_roms_path_depth):
                                rom_vault_relative_path = "../" + rom_vault_relative_path
                            actual_file_relative_path = rom_vault_relative_path + rom_name
                            try:
                                os.makedirs(frontend_roms_folder, exist_ok=True)
                                os.symlink(src=actual_file_relative_path, dst=frontent_linked_file_path)
                            except FileExistsError:
                                print(f"File already exists: {frontent_linked_file_path}")
                            except Exception as e:
                                print(f"Error creating symlink for {game_name}: {e}")
                                print(f"Game Info: {file}")
                            finally:
                                print(f"Created symlink: {actual_file_relative_path} to {frontent_linked_file_path}")
                            
                        
                # try:
                #     create_symlink(system, game_info)
                # except Exception as e:
                #     print(f"Error creating symlink for {system}: {e}")
                #     print(f"Game Info: {game_info}")
            
        else:
            print(f"Symlink file not found: {symlink_file}")

    # print(json.dumps(all_symlink_files, indent=2, sort_keys=True))

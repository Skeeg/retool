import os
import json
from glob import glob

# Environment variables in a dictionary
env_vars = {
    'MAP_FILE': os.environ.get('MAP_FILE'),
    'BASE_1G1R_DIRECTORY': os.environ.get('BASE_1G1R_DIRECTORY'),
    'BASE_MEDIA_DIRECTORY': os.environ.get('BASE_MEDIA_DIRECTORY'),
    'DATS_SUBDIRECTORY': os.environ.get('DATS_SUBDIRECTORY'),
    'LINKS_SUBDIRECTORY': os.environ.get('LINKS_SUBDIRECTORY'),
    'ROM_VAULT_PATH': os.environ.get('ROM_VAULT_PATH'),
    'MEDIA_VAULT_PATH': os.environ.get('MEDIA_VAULT_PATH'),
    'LINK_MEDIA_FILES': os.environ.get('LINK_MEDIA_FILES'),
    'OVERWRITE_LINK': os.environ.get('OVERWRITE_LINK'),
    'QUIET_MODE': os.environ.get('QUIET_MODE')
}

def get_symlink_files(directory):
    return sorted([filename for filename in os.listdir(directory) if filename.endswith(".symlinkdata.json")])

def match_dat_filename(truncated_string, full_filenames):
    for filename in full_filenames:
        if filename.startswith(truncated_string + ' ('):
            return filename
    return None

def walk_directory(base_path):
    result = {}
    for root, dirs, files in os.walk(base_path):
        for directory in dirs:
            directory_path = os.path.join(root, directory)
            relative_path = os.path.relpath(directory_path, base_path)
            result[relative_path] = [file for file in os.listdir(directory_path)]
    return result

def create_symlink(src, dst, overwrite_link=False):
    try:
        if overwrite_link:
            if os.path.exists(dst):
                os.remove(dst)
                print(f"Removed existing symlink: {dst}")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst):
            os.symlink(src=src, dst=dst)
            print(f"Created symlink: {src} to {dst}")
        else:
            if not env_vars['QUIET_MODE'] == "true":
                print(f"Link already exists: {dst}")
    except FileExistsError:
        if not env_vars['QUIET_MODE'] == "true":
            print(f"File exists: {dst}")
    except PermissionError:
        print(f"Permission denied: {dst}")
    except Exception as e:
        print(f"Error creating symlink: {e}")

if __name__ == "__main__":
    # Load the map file
    with open(env_vars['MAP_FILE'], 'r') as json_file:
        map_data = json.load(json_file)
        
    dats_directory = os.path.normpath(env_vars['DATS_SUBDIRECTORY'])
    links_directory = os.path.normpath(env_vars['LINKS_SUBDIRECTORY'])
    all_symlink_files = get_symlink_files(dats_directory)

    for system in map_data['Systems']:
        full_system = map_data['Systems'][system]
        frontend_folders = {}
        for frontend in full_system['frontends']:
            frontend_folders[frontend] = {}
            frontend_folders[frontend]['rom'] = {}
            frontend_folders[frontend]['media'] = {}
            frontend_folders[frontend]['base'] = os.path.join(
                os.path.normpath(links_directory),  
                os.path.normpath(frontend))
            
            base_path_test = os.path.normpath(frontend_folders[frontend]['base'])
            roms_path_test = os.path.normpath(full_system['frontends'][frontend]['roms_path']).lstrip('/')
            join_test = os.path.join(base_path_test, roms_path_test)
            frontend_folders[frontend]['rom']['links'] = os.path.join(
                os.path.normpath(frontend_folders[frontend]['base']), 
                os.path.normpath(full_system['frontends'][frontend]['roms_path']).lstrip('/'))
            frontend_folders[frontend]['media']['links'] = os.path.join(
                os.path.normpath(frontend_folders[frontend]['base']), 
                os.path.normpath(full_system['frontends'][frontend]['media_path']).lstrip('/'))
            frontend_folders['roms_physical_path'] = os.path.join(
                os.path.normpath(env_vars['ROM_VAULT_PATH']),
                os.path.normpath(full_system['roms_folder']))
            frontend_folders['media_physical_path'] = os.path.join(
                os.path.normpath(env_vars['MEDIA_VAULT_PATH']),
                os.path.normpath(full_system['screenscraper_folder']))
        symlink_file = match_dat_filename(map_data['Systems'][system]['datfile'], all_symlink_files)
        if env_vars['LINK_MEDIA_FILES'] == "true": media_files = walk_directory(frontend_folders['media_physical_path']);
        if symlink_file:
            with open(os.path.join(dats_directory, symlink_file), 'r') as json_file:
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
                            actual_file_path = os.path.join(
                                frontend_folders['roms_physical_path'], 
                                rom_name['full'] + full_system['linked_extension'])
                            frontend_linked_file_path = os.path.join(
                                frontend_folders[frontend]['rom']['links'], 
                                rom_name[rom_name_preference] + full_system['linked_extension'])
                            actual_file_relative_path = os.path.relpath(
                                os.path.dirname(actual_file_path),
                                os.path.dirname(frontend_linked_file_path))
                            create_symlink(
                                src=os.path.join(
                                    actual_file_relative_path,
                                    os.path.basename(actual_file_path)),
                                dst=frontend_linked_file_path, 
                                overwrite_link=env_vars['OVERWRITE_LINK'])
                            
                            if env_vars['LINK_MEDIA_FILES'] == "true":
                                frontend_media_paths = map_data['frontends'][frontend]['media_paths']
                                for media_path in frontend_media_paths:
                                    actual_media_asset_path = frontend_media_paths[media_path]
                                    frontend_asset_path = media_path
                                    matched_media_files = []
                                    try:
                                        for media_file in media_files[actual_media_asset_path]:
                                            if rom_name['full'] in media_file:
                                                matched_media_files.append(media_file)
                                        
                                        mapped_media_filenames = []
                                        for matched_filenames in matched_media_files:
                                            mapped_media_extension = os.path.splitext(matched_filenames)[1]
                                            mapped_media_filenames.append({'preffered_name': rom_name[rom_name_preference] + mapped_media_extension, 'actual_name': rom_name['full'] + mapped_media_extension})
                                        
                                        for item in mapped_media_filenames:
                                            actual_media_file_path = os.path.join(
                                                frontend_folders['media_physical_path'], 
                                                os.path.join(actual_media_asset_path, item['actual_name']))
                                            frontend_linked_media_file_path = os.path.join(
                                                frontend_folders[frontend]['media']['links'],
                                                os.path.join(frontend_asset_path, item['preffered_name']))
                                            actual_media_file_relative_path = os.path.relpath(
                                                os.path.dirname(actual_media_file_path), 
                                                os.path.dirname(frontend_linked_media_file_path))
                                            create_symlink(
                                                src=os.path.join(
                                                    actual_media_file_relative_path,
                                                    os.path.basename(actual_media_file_path)),
                                                dst=frontend_linked_media_file_path, 
                                                overwrite_link=env_vars['OVERWRITE_LINK'])

                                    except KeyError:
                                        print(f"Media folder not found: {frontend_folders['media_physical_path']}/{actual_media_asset_path}")
        else:
            if map_data['Systems'][system]['datsource'] == "none" and map_data['Systems'][system]['link_all'] == True :
                rom_files = sorted(os.listdir(frontend_folders['roms_physical_path']))
                for rom in rom_files:
                    for frontend in full_system['frontends']:
                        actual_file_path = os.path.join(
                            frontend_folders['roms_physical_path'], 
                            rom)
                        frontend_linked_file_path = os.path.join(
                            frontend_folders[frontend]['rom']['links'], 
                            rom)
                        actual_file_relative_path = os.path.relpath(
                            os.path.dirname(actual_file_path),
                            os.path.dirname(frontend_linked_file_path))
                        create_symlink(
                            src=os.path.join(
                                actual_file_relative_path,
                                os.path.basename(actual_file_path)),
                            dst=frontend_linked_file_path, 
                            overwrite_link=env_vars['OVERWRITE_LINK'])
                        if env_vars['LINK_MEDIA_FILES'] == "true":
                            rom_name = os.path.splitext(rom)[0]
                            frontend_media_paths = map_data['frontends'][frontend]['media_paths']
                            for media_path in frontend_media_paths:
                                actual_media_asset_path = frontend_media_paths[media_path]
                                frontend_asset_path = media_path
                                matched_media_files = []
                                try:
                                    for media_file in media_files[actual_media_asset_path]:
                                        if rom_name in media_file:
                                            matched_media_files.append(media_file)
                                    
                                    mapped_media_filenames = []
                                    for matched_filenames in matched_media_files:
                                        mapped_media_extension = os.path.splitext(matched_filenames)[1]
                                        mapped_media_filenames.append({'preffered_name': rom_name + mapped_media_extension, 'actual_name': rom_name + mapped_media_extension})
                                    
                                    for item in mapped_media_filenames:
                                        actual_media_file_path = os.path.join(
                                            frontend_folders['media_physical_path'], 
                                            os.path.join(actual_media_asset_path, item['actual_name']))
                                        frontend_linked_media_file_path = os.path.join(
                                            frontend_folders[frontend]['media']['links'],
                                            os.path.join(frontend_asset_path, item['preffered_name']))
                                        actual_media_file_relative_path = os.path.relpath(
                                            os.path.dirname(actual_media_file_path), 
                                            os.path.dirname(frontend_linked_media_file_path))
                                        create_symlink(
                                            src=os.path.join(
                                                actual_media_file_relative_path,
                                                os.path.basename(actual_media_file_path)),
                                            dst=frontend_linked_media_file_path, 
                                            overwrite_link=env_vars['OVERWRITE_LINK'])
                                except KeyError:
                                    print(f"Media folder not found: {frontend_folders['media_physical_path']}/{actual_media_asset_path}")
            else:
                print(f"Dat file not found: {map_data['Systems'][system]['datfile']} in {dats_directory}")

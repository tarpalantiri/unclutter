#!/usr/bin/python3
# [Author]
# Tehseen Sajjad
# [Summary]
# A small personal script that unclutters my desktop when working on an assignment or lab project.
# [Usage/Requirements]
# * Python > 3.5.x
# * files need to have '-' characters in their name.
# * The second word after the first '-' will be the folder to which the files will be moved.
# * Names of the folders are changed to title cases.
import lib

if __name__ == '__main__':
    Handle = lib.FileHandler()
    file_paths_dict = Handle.get_paths()
    if file_paths_dict:
        Handle.make_folder(file_paths_dict)
    else:
        lib.prompt(lib.NO_WORK_FILES_TO_COPY_MESSAGE)
    Handle.move_files(file_paths_dict)

    print("Moved Files: ")
    for folder, files in file_paths_dict.items():
        print(f"+-{lib.get_name_from_path(folder)}")
        for file in files:
            print(f'|----{lib.get_name_from_path(file)}')

    lib.prompt("Done!")

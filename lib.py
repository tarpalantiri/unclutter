import os
from shutil import move
from json import load

# Constants and settings load------------------------------------------------------------
SETTINGS_FILE_NOT_FOUND = "You need settings.json in the script directory..."

def prompt(msg=''):
    print(msg)
    input("Press ENTER to exit ... ")
    exit()

try:
    settings = load(open('settings.json'))
except FileNotFoundError:
    prompt(SETTINGS_FILE_NOT_FOUND)

DIR_ENTRY_OBJECTS_COLLECTION_ERROR = settings['errors']['DIR_ENTRY_CREATION_ERROR']
FOLDERS_CREATION_ERROR = settings['errors']['FOLDER_CREATION_ERROR']
NO_WORK_FILES_TO_COPY_MESSAGE = settings['messages']['NO_FILES_TO_COPY_MESSAGE']
FILE_MOVE_ERROR = settings["errors"]["FILE_MOVE_ERROR"]

isTestRun = settings['test_run']
if isTestRun:
    WORKSPACE_PATH = settings['test_dir_path']
else:
    WORKSPACE_PATH = settings['workspace_path']
#----------------------------------------------------------------------------------------

def get_name_from_path(path_str):
    return path_str.split('\\')[-1]

class FileHandler:
    
    def __init__(self):
        self.dir_entries = None
        with os.scandir(WORKSPACE_PATH) as dirObj:
            try:
                self.dir_entries = [file_entry for file_entry in dirObj if file_entry.is_file() and '-' in file_entry.name] # Find out why generators dont work
            except:
                prompt(DIR_ENTRY_OBJECTS_COLLECTION_ERROR)
        
        self.folderToFilesDict = {} 
    
    def get_paths(self):
        for fileObj in self.dir_entries:
            filename, extension = fileObj.name.split('.')
            cat = filename.split('-')[1].upper()
            
            folderPath = os.path.join(WORKSPACE_PATH, cat)
            filePath = os.path.join(WORKSPACE_PATH, fileObj.name)
            
            # Populate Dict{Folder-Path : [File-Paths]}
            if folderPath not in self.folderToFilesDict.keys():
                self.folderToFilesDict[folderPath] = []
            self.folderToFilesDict[folderPath].append(filePath)          

        if self.folderToFilesDict and len(self.folderToFilesDict) < 1:
            return None
        return self.folderToFilesDict

    def make_folder(self, path_dict={}):
        try:
            for path in path_dict.keys():
                if not os.path.exists(path):
                    os.mkdir(path)
        except:
            prompt(FOLDERS_CREATION_ERROR)
    
    def move_files(self, path_dict):
        try:
            for folder, filesList in path_dict.items():
                for filePath in filesList:
                    dst = os.path.join(folder, filePath.split('\\')[-1])
                    move(filePath, dst)
        except:
            prompt(FILE_MOVE_ERROR)
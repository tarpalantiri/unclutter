import os
from shutil import move
from json import load
from datetime import datetime

SETTINGS_FILE_NOT_FOUND = "You need settings.json in the script directory..."
SETTINGS_FILE_IO_ERROR = "Cannot read settings file"

def prompt(msg=''):
    print(msg)
    input("Press ENTER to exit ... ")
    exit()

try:
    settings = load(open('settings.json'))
except FileNotFoundError:
    prompt(SETTINGS_FILE_NOT_FOUND)
except IOError:
    prompt(SETTINGS_FILE_IO_ERROR)

DIR_ENTRY_OBJECTS_COLLECTION_ERROR = settings['errorMessages']['DIR_ENTRY_CREATION_ERROR']
FOLDERS_CREATION_ERROR = settings['errorMessages']['FOLDER_CREATION_ERROR']
NO_WORK_FILES_TO_COPY_MESSAGE = settings['casualPrompts']['NO_FILES_TO_COPY_MESSAGE']
FILE_MOVE_ERROR = settings["errorMessages"]["FILE_MOVE_ERROR"]
FOLDER_NAME_DETERMINER = settings["programSettings"]["folderNameDeterminer"] - 1
DATETIME_FORMAT = settings["programSettings"]["dateTimeFormat"]
ADD_DATETIME = settings["programSettings"]["addDateTime"]
TODAY = datetime.now().strftime(DATETIME_FORMAT)
isTestRun = settings["programSettings"]['testRun']
if isTestRun:
    WORKSPACE_PATH = settings["programSettings"]['testDirPath']
else:
    WORKSPACE_PATH = settings["programSettings"]['workspacePath']


def get_name_from_path(path_str):
    return path_str.split('\\')[-1]

def get_folder_name(file_name):
    folder_name_string = "{date} - {name}"
    folder_name = file_name.split('-')[FOLDER_NAME_DETERMINER].upper()
    if ADD_DATETIME:
        return folder_name_string.format(date=TODAY, name=folder_name)
    else:
        return folder_name

class FileHandler:
    
    def __init__(self):
        self.dir_entries = None
        with os.scandir(WORKSPACE_PATH) as dirObj:
            try:
                self.dir_entries = [file_entry for file_entry in dirObj if file_entry.is_file() and '-' in file_entry.name] # Find out why generators dont work here
            except:
                prompt(DIR_ENTRY_OBJECTS_COLLECTION_ERROR)
        
        self.folderToFilesDict = {} 
    
    def get_paths(self):
        for fileObj in self.dir_entries:
            filename, extension = fileObj.name.split('.')
            folder_name = get_folder_name(filename)
            
            folderPath = os.path.join(WORKSPACE_PATH, folder_name)
            filePath = os.path.join(WORKSPACE_PATH, fileObj.name)
            
            # Populate Dict{ FolderPath : [FilePaths] }
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

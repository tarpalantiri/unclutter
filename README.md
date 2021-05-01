## Unclutter
Personal program to unclutter my desktop after researching an assignment.

## Usage
The program determines if a file is to be organized by if it has the *dash* (-) character in the file name
Running the script in a shell or double clicking it will start the execution

## Settings
The settings are located in `settings.json` file in the main directory.
Settings description:
|Keyword|Description  |
|--|--|
|`workspacePath`|Tells the program where to look for its work|
| `testDirPath` | A test folder for testing the execution of the program in a safe environment |
|`testRun`|Tells the program weather to run in test folder or workspace folder |
|`folderNameDeterminer`|Folder name accessor. Determines the position of the name of the folder in the name of the files being worked on. *example* in this-is-a-name.pdf has this:1, is:2 ...|
|`addDateTime`| Determines weather to add date-time info to the folder names|
|`dateTimeFormat`|Python date-time format string. Formatting for the date time. https://www.w3schools.com/python/python_datetime.asp

## Todo

 - [X] Add option to change which text determines the folder names
 - [X] Option to add Date/Time to the folder name
 - [ ] Change program to a continous loop
	 - [ ] Caching of created folders
	 - [ ] Temporary object creation
 - [ ] Migrate from terminal to GUI with tkinter

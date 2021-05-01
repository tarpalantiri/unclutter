
## Info
Personal program to unclutter my desktop after researching an assignment.<br>
The program determines if a file is to be organized, if it has the *dash* (-) character in the file name.

## Usage
Run `unclutter.py`

## Install
`git clone https://tarpalantiri/uncluter` or download the repository and extract.

## Settings

The settings are located in `settings.json` file in the main directory.
Settings description:

|Keyword|Description| Value|
|--|--|--|
|`workspacePath`|Tells the program where to look for its work|Windows Path string|
| `testDirPath` | A test folder for testing the execution of the program in a safe environment |Windows Path string|
|`testRun`|Tells the program weather to run in test folder or workspace folder | Boolean **true** / **false** |
|`folderNameDeterminer`|Folder name accessor. Determines the position of the name of the folder in the name of the files being worked on. *example* in `this-is-a-name.pdf` has `this:1, is:2` ...| Integer |
|`addDateTime`| Determines weather to add date-time info to the folder names| Boolean **true** / **false** |
|`dateTimeFormat`|Python date-time format string. Formatting for the date time string. https://www.w3schools.com/python/python_datetime.asp | Python Datetime Format String |


## Todo

- [X] Add option to change which text determines the folder names
- [X] Option to add Date/Time to the folder name
- [ ] Change program to a continuous loop
- [ ] Migrate from terminal to GUI with tkinter

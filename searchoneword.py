import os
import re

# Folder to be searched
folder_path = './'  # assuming you're searching the current directory, modify as needed

# Phrase to search
search_phrase = '开启对话' #搜索内容写这里
search_pattern = re.compile(search_phrase)

# Get all files in folder
file_list = []
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        file_list.append(os.path.join(dirpath, filename))

# Search for the phrase in each file immediately after reading it
matches = []  # Initialize an empty list to store match details
file_match_count = 0  # Initialize the count of files with matches
progress = 0
for file_name in file_list:
    progress += 1
    print(f"Searching file {progress} of {len(file_list)}: {file_name}")
    match_in_file = False
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if search_pattern.search(line):
                    matches.append(f"Found '{search_phrase}' at line {i+1} of file '{file_name}'")  # Add match details to the list
                    match_in_file = True  # Set the flag to True if a match is found
    except (UnicodeDecodeError, PermissionError,FileNotFoundError):  # Catch both exceptions
        pass  # If an exception occurs, do nothing and move on to the next file
    if match_in_file:
        file_match_count += 1  # Increment the count if a match was found in the file
    print("\033[A"*5)  # Move the cursor up 5 lines to overwrite the previous output

print(f"Search completed. Searched {len(file_list)} files, found matches in {file_match_count} files.")
print("Match details:")
for match in matches:  # Print all match details stored in the list
    print(match)

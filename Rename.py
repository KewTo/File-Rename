import os

""" Renaming a group of files by entering the entire folder directory name, current filename, and the new desired
filename. It will rename all files that has the current filename: for example all files that has the word 'TWICE'
in the filename will be replaced with twice if new_filename 'twice' is entered and current_filename 'TWICE' is entered. """

# Enter entire folder directory name
folder = input('Please copy and paste folder path: ')

# Enter whichever part of the current filename you would like changed
current_filename = input('Please enter which part of the current filename you would like to change: ')

# Enter the new change to replace whatever input placed in current_filename
new_filename = input('Please enter what you would like to change it to: ')


# Replace old_filename with new_filename, replacing all current filename with a new desired filename
def main():
    # Goes through every file in specified folder
    paths = (os.path.join(root, filename)
             for root, _, filenames in os.walk(folder)
             for filename in filenames)
    for path in paths:
        newname = path.replace(current_filename, new_filename)
        if newname != path:
            os.rename(path, newname)


if __name__ == '__main__':
    main()

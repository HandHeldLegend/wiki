import os

def rename_md_files():
    # Get the current directory
    current_directory = os.getcwd()

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Rename .md files replacing spaces with dashes
    for file in files:
        if file.endswith('.md'):
            new_name = file.replace(' ', '-')
            os.rename(os.path.join(current_directory, file), os.path.join(current_directory, new_name))
            print(f'Renamed {file} to {new_name}')

if __name__ == "__main__":
    rename_md_files()
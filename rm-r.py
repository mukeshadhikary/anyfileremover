import os
import argparse

def remove_files(directory, file_extension):
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
        print(f"All files with the '{file_extension}' extension removed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove files with a specific extension from a directory recursively.")
    parser.add_argument("directory", type=str, help="The directory path to start the search and remove files.")
    parser.add_argument("file_extension", type=str, help="The file extension to remove (e.g., .srt).")
    
    args = parser.parse_args()
    
    if os.path.isdir(args.directory):
        remove_files(args.directory, args.file_extension)
    else:
        print("The provided path is not a valid directory.")

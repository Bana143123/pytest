# Write a Python program that scans a directory and generates a summary file, 
# summary.txt, containing:

# The total number of files in the directory.
# The total size of all files (in bytes).
# A list of all files with their sizes, sorted by size (largest first).

import os

def scan_directory(directory):
    file_sizes={}
    print(directory)

    for root,_, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            print(file_path)
            if os.path.isfile(file_path):
                file_sizes[file_path] = os.path.getsize(file_path)
    return file_sizes


def main():
    directory_to_scan = "checking_j"
    file_size= scan_directory(directory_to_scan)
    print(file_size)

if __name__ == "__main__":
    main()

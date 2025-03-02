import os

def walk_recursive(path):
    """Generator function to yield (dirpath, dirnames, filenames) for each subdirectory recursively."""
    if not os.path.isdir(path):  # Base case: path is not a directory
        return

    dirnames, filenames = [], []

    for entry in os.listdir(path):  # List all contents of the directory
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            dirnames.append(entry)  # It's a directory
        else:
            filenames.append(entry)  # It's a file

    yield path, dirnames, filenames  # Yield current directory data

    for dirname in dirnames:  # Recursively explore subdirectories
        yield from walk_recursive(os.path.join(path, dirname))

# Example usage
for dirpath, dirnames, filenames in walk_recursive("/your/directory/path"):
    print(f"Directory: {dirpath}, Subdirectories: {dirnames}, Files: {filenames}")

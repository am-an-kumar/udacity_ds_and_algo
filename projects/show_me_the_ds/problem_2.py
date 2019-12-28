import os


def find_files(suffix, path):
    """
     Find all files beneath path with file name suffix.

     Note that a path may contain further subdirectories
     and those subdirectories may also contain further subdirectories.

     There are no limit to the depth of the subdirectories can be.

        :params: -
            suffix(str) - suffix if the file name to be found
            path(str) - path of the file system
        :output: -
            files(list) - list fo files with suffix present inside folder
    Time complexity - O(n), where n = number of files inside a folder
    """
    match_files = []

    if not os.path.isdir(path):
        return match_files

    file_paths = os.listdir(path)
    for file_path in file_paths:
        file_path_abs = os.path.join(path, file_path)

        if os.path.isdir(file_path_abs):
            match_files += find_files(suffix, file_path_abs)
        else:
            if file_path_abs.endswith(suffix):
                match_files.append(file_path_abs)

    return match_files


# tests for relative paths
print("Test 1")
print(find_files('.exe', '../'))

print("Test 2")
print(find_files('.py', './'))

# test for absolute path, this path contained the test directory to test
print("Test 3")
print(find_files('.c', r'C:\Users\amank\Downloads\testdir'))

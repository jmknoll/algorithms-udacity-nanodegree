import os


def find_files(suffix, path):
    files = []
    for el in os.listdir(path):
        fullpath = os.path.join(path, el)
        # base case
        if os.path.isfile(fullpath) and fullpath.endswith('.c'):
            files.append(fullpath)
        # recursive case
        if os.path.isdir(fullpath):
            files += find_files(suffix, fullpath)

    return files


print(find_files('.c', 'testdir'))

import os


def find_files(suffix, path):
    # validate edge cases
    if (not path) or (not os.path.isdir(path)):
        return []

    files = []
    if not os.listdir(path):
        return []
    for el in os.listdir(path):
        fullpath = os.path.join(path, el)
        # base case
        if os.path.isfile(fullpath) and fullpath.endswith(".c"):
            files.append(fullpath)
        # recursive case
        if os.path.isdir(fullpath):
            files += find_files(suffix, fullpath)

    return files


print(find_files(".c", "testdir"))
# ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

print(find_files(".c", "not a path"))
# []

print(find_files(".c", None))
# []

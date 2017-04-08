import os
import sys


def getroot():
    if len(sys.argv) == 1:
        path = ''
    else:
        path = sys.argv[1]

    if os.path.isabs(path):
        tree_root = path
    else:
        tree_root = os.path.join(os.getcwd(), path)

    return tree_root


def getdirlist(path):
    dirlist = os.listdir(path)
    dirlist = [name for name in dirlist if name[0] != '.']
    dirlist.sort()
    return dirlist


def traverse(path):
    os.chdir(path)
    dirlist = getdirlist(path)
    if 'trash.txt' in dirlist:
        os.system('rm trash.txt')

    for fname in dirlist:
        path2file = os.path.join(path, fname)
        if os.path.isdir(path2file):
            traverse(path2file)


if __name__ == '__main__':
    root = getroot()
    traverse(root)

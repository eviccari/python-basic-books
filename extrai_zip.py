# coding: utf-8

import os
import zipfile
import sys


def main(path):
    if not os.path.exists(path):
        print("File {} not exists".format(path))
        sys.exit(1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Unzip completed")


if __name__:
    main(sys.argv[1])
    sys.exit(0)

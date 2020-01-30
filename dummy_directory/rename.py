import re
import os
import random
import argparse

# Give every file in a directory a randomly-generated named

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--directory", required=False, help="Path to the directory to have its contents renamed", default="./")
args = vars(ap.parse_args())

def rename_all():
    f = args["directory"] + "/"
    original_names = os.listdir(f)

    for name in original_names:
        name = f + name
        _, extension = os.path.splitext(name)
        new_name = f + r"%010x" % random.randint(0, 1000000000000) + extension
        if re.search(f + "\d+.*", name) is not None:
            os.rename(name, new_name)

if __name__ == '__main__':
    rename_all()

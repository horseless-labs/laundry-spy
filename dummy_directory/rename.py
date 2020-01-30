import re
import os
import random

# Give every file in a directory a randomly-generated named

def rename_all():
    original_names = os.listdir()

    for name in original_names:
        _, extension = os.path.splitext(name)
        new_name = r"%010x" % random.randint(0, 1000000000000) + extension
        if re.search("\d+.*", name) is not None:
            os.rename(name, new_name)

if __name__ == '__main__':
    rename_all()

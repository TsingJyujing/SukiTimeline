#!/usr/bin/python3

import argparse
import os
import shutil
import sys


def parameter_parse():
    ap = argparse.ArgumentParser(
        prog="docker_start.py",
        description="Entry point for starting Docker container"
    )
    ap.add_argument(
        "--mode",
        dest="mode",
        default="runserver",
        help="mode can be runserver or createsuperuser, using docker run -it while creating super user.",
        type=str
    )
    return ap.parse_args(sys.argv[1:])


def init_db_if_not_exist():
    """
    Trying to find the database, if db not found, initialize one
    :return:
    """
    if not os.path.exists("/data/db.sqlite3"):
        print("Database file not exist, creating...")
        os.system("/usr/bin/python3 manage.py migrate")
        shutil.move("db.sqlite3", "/data/db.sqlite3")
    else:
        print("Database check passed.")


def mount_data_config(src: str, target: str):
    """
    Mount all the data (database file) and config file
    :return:
    """
    # Only mount one layer file in this app
    # for _, _, files in os.walk(src, topdown=False):
    #    for file in files:
    for file in (f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))):
        print("Mounting files from {} to {}...".format(src, target))
        target_file = os.path.join(target, file)
        if os.path.exists(target_file):
            os.remove(target_file)
            print("{} already in target, removed.".format(target_file))
        print("Mount file: {} -> {}".format(os.path.join(src, file), target_file))
        os.symlink(os.path.join(src, file), target_file)


if __name__ == '__main__':
    pr = parameter_parse()
    init_db_if_not_exist()
    mount_data_config("/data", "/app")
    if pr.mode == 'runserver':
        os.system("/usr/bin/python3 manage.py runserver --noreload 0.0.0.0:80")
    elif pr.mode == 'createsuperuser':
        os.system("/usr/bin/python3 manage.py createsuperuser")
    else:
        raise Exception("Unsupport mode: {}".format(pr.mode))

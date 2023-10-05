#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local, task
from datetime import datetime
from os import path


@task
def do_pack():
    """Function that archive web_static folder """
    mkdir = "mkdir -p versions"
    datetime = datetime.now()
    date = datetime.strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(file))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, file)).succeeded:
        return file
    else:
        return None
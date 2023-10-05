#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local, task
from datetime import datetime
from os import path


@task
def do_pack():
    """Function that archive web_static folder """

    if path.exists('versions') is False:
        local('mkdir versions')
    datetime = datetime.now()
    date = datetime.strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    local('tar -cvzf {} web_static'.format(file))
    if file:
        return file
    else:
        return None

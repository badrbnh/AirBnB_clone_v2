#!/usr/bin/python3
"""  script (based on the file 1-pack_web_static.py"""


from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['ubuntu@3.85.148.98', '34.234.204.60']


@task
def do_deploy(archive_path):
    """ method to deploy"""
    try:
        if not local("test -e {}".format(archive_path)).succeeded:
            return False
        file_withex = os.path.basename(archive_path)
        file_noex, ex = os.path.splitext(file_withex)
        put(archive_path, "/tmp/")
        run("rm -f {}".format(archive_path))
        run("mkdir -p /data/web_static/releases/{}/".format(file_noex))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_withex, file_noex))
        run("rm /tmp/{}".format(file_withex))
        run("mv /data/web_static/releases/{0}/web_static/* "
            "/data/web_static/releases/{0}/".format(file_noex))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_noex))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(file_noex))
        print("New version deployed!")
        return True
    except Exception:
        return False

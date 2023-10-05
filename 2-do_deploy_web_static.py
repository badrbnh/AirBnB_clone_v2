#!/usr/bin/python3
""" Fabric script to distribute an archive to web servers """

from fabric.api import env, put, run
from os.path import exists


env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['54.87.180.223', '52.23.245.155']  # Replace with your server IPs

def do_deploy(archive_path):
    """ Distribute an archive to web servers """
    if not exists(archive_path):
        return False

    try:
            archive_name = archive_path.split("/")[-1]
            no_extension = archive_name.split(".")[0]
            remote_folder = "/data/web_static/releases/{}".format(no_extension)

            # Upload the archive to the /tmp/ directory on the server
            put(archive_path, "/tmp/{}".format(archive_name))

            # Uncompress the archive to the specified folder
            run("mkdir -p {}".format(remote_folder))
            run("tar -xzf /tmp/{} -C {}".format(archive_name, remote_folder))

            # Delete the uploaded archive from the server
            run("rm /tmp/{}".format(archive_name))

            # Move contents to the appropriate location
            run("mv {}/web_static/* {}".format(remote_folder, remote_folder))

            # Remove the old symbolic link
            run("rm -rf /data/web_static/current")

            # Create a new symbolic link
            run("ln -s {} /data/web_static/current".format(remote_folder))

            return True

    except Exception as e:
            return False

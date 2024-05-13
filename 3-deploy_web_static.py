#!/usr/bin/python3
"""
Fabric script for creating and distributing a web application archive to
multiple web servers. This script extends the functionality of the file
2-do_deploy_web_static.py by automating the process of creating the archive
before deployment.

Execution:
    To execute the deployment process, use the following command:
        fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu

Requirements:
    - Fabric library for Python (install via pip: pip install fabric)

Configuration:
    - Configure the env.hosts variable with the IP addresses or hostnames of
    the target web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['3.89.160.178', '35.175.63.135']


def do_pack():
    """
    Generates a compressed archive of the web_static directory.

    Returns:
        str: The file path of the generated archive if successful, None
        otherwise.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the designated web servers and deploys it.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    if exists(archive_path) is False:
        print(f"Archive '{archive_path}' not found.")
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        print("Deployment completed successfully.")
        return True
    except Exception:
        return False


def deploy():
    """
    Orchestrates the process of creating and distributing an archive to the
    web servers.

    Returns:
        bool: True if deployment was successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

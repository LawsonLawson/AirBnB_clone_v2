#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers based on
1-pack_web_static.py.
"""


from fabric.api import put, run, env
from os.path import exists

# Define remote hosts
env.hosts = ['3.89.160.178', '35.175.63.135']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): Path to the archive file to deploy.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Check if archive exists
    if not exists(archive_path):
        return False

    try:
        # Extract archive name and remove extension
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]

        # Define paths
        releases_path = "/data/web_static/releases/"
        tmp_path = "/tmp/"

        # Upload archive to server
        put(archive_path, tmp_path)

        # Create directory for the new release
        run('mkdir -p {}{}/'.format(releases_path, folder_name))

        # Extract archive contents to the new release directory
        run('tar -xzf {}{} -C {}{}/'.format(tmp_path, archive_name,
            releases_path, folder_name))

        # Remove temporary archive
        run('rm {}{}'.format(tmp_path, archive_name))

        # Move contents of extracted directory to web server's folder
        run('mv {}{}/web_static/* {}{}/'.format(releases_path, folder_name,
            releases_path, folder_name))

        # Remove unnecessary directory
        run('rm -rf {}{}/web_static'.format(releases_path, folder_name))

        # Update symbolic link to current release
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(releases_path,
            folder_name))

        return True

    except Exception as exception:
        print("Exception:", exception)
        return False

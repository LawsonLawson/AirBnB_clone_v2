#!/usr/bin/python3
"""
Fabric script to generate a compressed archive (tgz) of the web_static directory.
Usage: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates a compressed archive of the web_static directory.

    Returns:
        str: Name of the archive if successfully created, otherwise None.
    """

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = 'web_static_' + timestamp + '.tgz'
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None

import sys
import importlib
import subprocess
from importlib import metadata
from packaging import version
import os


def is_installed(name, version_spec=None):
    try:
        installed_version = metadata.version(name)
        if version_spec is None or version_spec == '':
            return True  # Any version is acceptable
        else:
            return version.parse(installed_version) == version.parse(version_spec)
    except metadata.PackageNotFoundError:
        return False


def install_and_import(name, version_spec, uninstall_first=False):
    if not is_installed(name, version_spec):
        try:
            if uninstall_first:
                subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', name])
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{name}=={version_spec}' if version_spec else f'{name}'])
        except subprocess.SubprocessError as e:
            if not uninstall_first:
                install_and_import(name, version_spec, True)
            else:
                raise e


def change_version(new_version, uninstall_first=False):
    """Change the version of aplustools and restart the script."""
    install_and_import('aplustools', new_version, uninstall_first)
    os.execl(sys.executable, sys.executable, *sys.argv)


def get_env_version():
    # Check if the use of APLUSTOOLS_VERSION is skipped
    if os.getenv('SKIP_APLUSTOOLS_VERSION_ENV', 'false').lower() == 'true':
        return ''  # Replace with your default version
    else:
        return os.getenv('APLUSTOOLS_VERSION', '')


# Initial import with version from environment variable or default
initial_version = get_env_version()
install_and_import("aplustools", initial_version)

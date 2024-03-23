import os
import toml
import re

def handle_read_only_error(func, path, _):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


def modify_poetry_file(location, package_name: str, project_name: str, description: str = "", version: str = "0.0.1"):
    reg_name = r'(\[tool\.poetry](?:\n(?!\[[^][]*]).*)*\nname = ")[^"\n]*(?=")'
    reg_description = r'(\[tool\.poetry](?:\n(?!\[[^][]*]).*)*\ndescription = ")[^"\n]*(?=")'
    reg_version = r'(\[tool\.poetry](?:\n(?!\[[^][]*]).*)*\nversion = ")[^"\n]*(?=")'
    reg_package = r'(?<={include = ").*(?="})'
    with open(location, 'r', encoding='utf-8') as f:
        config = f.read()
    config = re.sub(reg_name, fr"\1{project_name}", config)
    config = re.sub(reg_description, fr"\1{description}", config)
    config = re.sub(reg_version, fr"\1{version}", config)
    config = re.sub(reg_package, package_name, config)
    with open(location, 'w', encoding="utf-8") as f:
        f.write(config)
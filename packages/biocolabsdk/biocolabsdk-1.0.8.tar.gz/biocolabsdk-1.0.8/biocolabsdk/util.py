import os
import pwd
import json
import getpass
from .identity import Identity
import requests

def empty(data: str):
    if (data is None) or (len(data) == 0):
        return True
    return False


def get_system_user():
    try:
        user = pwd.getpwuid(os.getuid())[0]
    except:
        user = os.environ.get('NB_USER', getpass.getuser())
    return user


def get_user_home_path():
    username = get_system_user()
    if username is None:
        return None

    pathDir = f"/home/{username}"
    try:
        with Identity(username):
            pathDir = os.path.expanduser(
                f"~{pwd.getpwuid(os.geteuid())[0]}")
    except:
        pass

    return pathDir

def get_user_study_root_path():
    return f"{get_user_home_path()}/studies"

def get_user_notebook_root_path():
    return f"{get_user_home_path()}/notebooks"

def get_user_app_root_path():
    return f"{get_user_home_path()}/apps"

def get_settings():
    obj = {}
    user_home_path = get_user_home_path()
    if user_home_path is None:
        return obj

    bio_key_file = f"{user_home_path}/.bioapi.key"
    if os.path.exists(bio_key_file):
        with open(bio_key_file) as f:
            try:
                obj = json.loads(f.read().strip())
            except:
                pass
            f.close()

    return obj

def get_studio_settings(
    private_studio_host: str = "http://127.0.0.1:11123", 
    private_studio_token: str = "",
    private_studio_email: str = "",
    private_studio_token_idx: int = 0
):
    obj = {}
    user_home_path = get_user_home_path()
    if user_home_path is None:
        return obj

    studio_token = private_studio_token
    studio_email = private_studio_email
    if (empty(studio_token) == True) or (empty(studio_email) == True):
        token_file = f"{user_home_path}/.local/share/.mybtk.json"
        if os.path.exists(token_file):
            with open(token_file) as f:
                try:
                    obj_tk = json.loads(f.read().strip())
                    if private_studio_token_idx < len(obj_tk):
                        if "email" in obj_tk[private_studio_token_idx]:
                            studio_email = obj_tk[private_studio_token_idx]["email"]

                        if "token" in obj_tk:
                            studio_token = obj_tk[private_studio_token_idx]["token"]
                except:
                    pass
                f.close()

    try:
        url_link = "{0}/pyapi/private/get_setting".format(private_studio_host)
        resp = requests.get(url_link, headers={
            "Content-Type": "application/json",
            "X-Email-Id": studio_email,
            "X-User-Token": studio_token
        })

        data = resp.json()
        if ("status" in data) and ("message" in data):
            if data["status"] == 0:
                obj = data["message"]
    except:
        pass

    return obj

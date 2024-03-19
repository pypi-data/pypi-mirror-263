import dbm, os, subprocess

_global = {
    "ARKHOS_GLOBAL_DOMAIN": os.environ.get("ARKHOS_GLOBAL_DOMAIN"),
    "APP_NAME": os.environ.get("APP_NAME"),
    "APP_API_KEY": os.environ.get("APP_API_KEY"),
    "LOG_LEVEL": "LOG",
    "log_buffer": [],
}


def set_up_local():
    project_root_dir = subprocess.getoutput("git rev-parse --show-toplevel")
    arkhos_dir = project_root_dir + "/.arkhos"

    # initialize .arkhos folder
    if not os.path.isdir(arkhos_dir):
        os.mkdir(arkhos_dir)

    arkhos_dbm_path = arkhos_dir + "/arkhos.dbm"
    _global["dbm"] = dbm.open(arkhos_dbm_path, "c")

def get(key, default_value=None):
    return _global["dbm"].get(key, default_value)

def set(key, value):
    _global["dbm"][key] = value

def log(body, level="LOG", type=None, status_code=None, metadata=None, event_at=None):
    print(f"Arkhos logging: {body}")

def log_flush():
    return

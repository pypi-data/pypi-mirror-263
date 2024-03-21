import os, stat
import requests
import time
from pathlib import Path
from glob import glob
from datetime import datetime as dt
from .utils import StdTime

def get_latest_file(path_pattern: str) -> Path:
    latest, latest_time = None, 0
    for f in glob(path_pattern, recursive=True):
        x = os.path.getmtime(f)
        if x > latest_time:
            latest_time = x
            latest = f

    assert latest is not None, f"target [{path_pattern}] doesn't exist"
    return Path(latest)

def Monitor(url, target):
    previous_snapshot = []
    def _poll():
        nonlocal previous_snapshot
        path = get_latest_file(target)
        if not path.exists(): return 

        if path.is_file():
            with open(path, "r") as f:
                lines = f.readlines()
                snapshot = lines[-100:]
        else:
            snapshot = os.listdir(path)
        if snapshot == previous_snapshot: return

        previous_snapshot = snapshot
        print(f"{StdTime.Timestamp()}: [{path}] changed")
        # print(snapshot)
        print("notifying server...")
        res = requests.post(url, json=dict(snapshot=list(snapshot)))
        c, t = res.status_code, res.text
        print(c, t)

    while True:
        try:
            _poll()
            time.sleep(3)
        except KeyboardInterrupt:
            print("killed")
            break

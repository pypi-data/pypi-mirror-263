import argparse
# import configparser
import os
import sys
import toml
import time
import subprocess
from loguru import logger
import inotify.adapters

__version__ = '0.0.8'

config = None

config_files = ['backrun.toml', os.path.expanduser('~/backrun.toml'), '/etc/backrun.toml']
def_config = next((file for file in config_files if os.access(file, os.R_OK)), None)

def read_config():
    try:
        config_path = sys.argv[1]
    except IndexError:
        config_path = def_config

    if config_path is None:
        print(f"Need .toml config file as first argument or {config_files}")
        sys.exit(1)

    with open(config_path) as fh:
        config = toml.load(fh)

    return config_path, config


def run_script(script_path, output_file, username=None, taskid=None, taskfile=None):
    with open(output_file, 'w') as f:

        env = os.environ.copy()
        if taskid:
            env["TASKID"] = taskid
        if taskfile:
            env["TASKFILE"] = taskfile

        if username:
            env['HOME'] = os.path.expanduser('~'+username)

        rc = subprocess.run([script_path], stdout=f, user=username, stderr=subprocess.STDOUT, env=env)
        return rc.returncode


def process_task(taskid: str):
        taskfile = os.path.join(config['taskdir'], taskid)
        with open(taskfile) as fh:
            script_name = fh.readline().strip()
        
        script_path = config['scripts'][script_name]['path']
        username = config['scripts'][script_name].get('user')
        log_path = os.path.join(config['logdir'], f'{taskid}.log')

        logger.info(f"task: {taskid!r} script: {script_name!r} user: {username!r}")
        code = run_script(script_path, log_path, username=username, taskid=taskid, taskfile=taskfile)
        os.unlink(taskfile)
        logger.info(f"finished task {taskid} {script_name!r} code: {code}")

def scan_tasks():
    for taskid in os.listdir(config['taskdir']):
        print(f"found task {taskid}")
        process_task(taskid)

def main():
    global config
    config_path, config = read_config()

    logger.remove()
    logger.add(sys.stdout, format="{message}")
    logger.add(config['logfile'], format="{time:YYYY-MM-DD at HH:mm:ss} {message}")

    logger.info(f"Start polling {config['taskdir']}, config: {config_path}")

    i = inotify.adapters.Inotify()
    i.add_watch(config['taskdir'])

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        if not filename:
            continue

        if filename.startswith('.'):
            continue

        if not 'IN_CLOSE_WRITE' in type_names:
            continue

        logger.info("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

        scan_tasks()


# coding:utf-8

import os
from queue import Queue
from typing import List

import pycountry
from xarg import add_command
from xarg import argp
from xarg import commands
from xarg import run_command

from ..utils import domain_database
from ..utils import domain_ranking

DEF_RETRIES: int = 100
MAX_RETRIES: int = 1000


@add_command("update-rankings", help="Update the ranking of domain names")
def add_cmd_update_rankings(_arg: argp):
    CURRENT_DIR = os.path.join(os.path.abspath("."), "rankings")
    _arg.add_argument("-d", "--dir", nargs=1, type=str, default=[CURRENT_DIR],
                      help=f"Download directory, default to {CURRENT_DIR}")
    _arg.add_argument("--retries", nargs=1, type=int, metavar="NUM",
                      default=[DEF_RETRIES], help="Maximum retries (less than "
                      f"{MAX_RETRIES}), default to {DEF_RETRIES}")


@run_command(add_cmd_update_rankings)
def run_cmd_update_rankings(cmds: commands) -> int:
    dir: str = os.path.abspath(cmds.args.dir[0])
    latest_dir: str = os.path.join(dir, "latest")
    if not os.path.exists(latest_dir):
        os.makedirs(latest_dir)
    assert os.path.isdir(latest_dir), f"{latest_dir} not an existing directory"
    database = domain_database(os.path.join(dir, "domains.csv"))
    cmds.logger.info(f"save rankings to directory: {dir}")
    retries: int = min(cmds.args.retries[0], MAX_RETRIES)
    queue: Queue[domain_ranking] = Queue()
    queue.put(domain_ranking())
    for country in pycountry.countries:
        queue.put(domain_ranking(country))
    entry: List[domain_ranking] = list()
    while not queue.empty():
        object = queue.get(block=False)
        if not object.download(latest_dir):
            if retries > 0:
                queue.put(object)
                retries -= 1
            continue
        entry.append(object)
    database.dump()
    for item in entry:
        cmds.logger.info({k: database.index(k) for k in item})
    return 0

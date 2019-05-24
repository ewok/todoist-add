#!/usr/bin/python3
from todoist import TodoistAPI
from pathlib import Path
from getpass import getpass
from pprint import pformat
import sys


class TD:
    store = Path.home().joinpath(".todoist")
    verbose = False

    def __init__(self):
        token, fromfile = self._load_token()
        if not fromfile:
            # if prompting for token, already interactive, so
            # show confirmation if the task is added.
            self.verbose = True
        self._api = TodoistAPI(token)

    def _load_token(self):
        """Load API token from file or user"""
        if self.store.exists():
            with open(self.store, "r") as f:
                return f.read().strip(), True
        else:
            return self._init_token(), False

    def _init_token(self):
        token = getpass("Todoist API token: ")
        if not token:
            raise Exception("API token is required.")
        with open(self.store, "w") as f:
            f.write(token)
        print("Saved to %s, please check permissions are secure." % self.store)
        return token

    def add(self, task):
        retval = self._api.quick.add(task)
        # Validate return value
        # Original input string may be truncated,
        # for example #myproject becomes a projectid field
        if not retval or not retval.get("content", "\x00") in task:
            raise Exception("Error: " + pformat(retval))
        if self.verbose:
            print("Added task to Todoist successfully.")


def main(args):
    """Todoist Quick-Add Task CLI, jeffgreenca

        Usage:
            $ td <task>

        Uses "quick add" syntax:
            $ td pickup milk tomorrow #errands @walking p1

    Persists API token in ~/.todoist, so be sure to secure it.
    """
    item = " ".join(args)
    t = TD()
    t.add(item)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
        print(main.__doc__)
    else:
        main(sys.argv[1:])

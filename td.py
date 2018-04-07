#!/usr/bin/python3
# Todoist Quick Add CLI
# jeffgreenca 2018
#
# A single-purpose tool to enable quick-add Todoist entries from the command line.
#
# Requires todoist-python
import sys
from pprint import pprint
from pathlib import Path

CONFIG_FILE = str(Path.home()) + '/.todoist'

def pdot():
  """Makeshift progress bar"""
  print('.', end='', flush=True)

# Configure
try:
  with open(CONFIG_FILE, 'r') as f:
    SECRET_KEY = f.read()
except FileNotFoundError:
  SECRET_KEY = input("Enter your API token (will be saved to %s): " % CONFIG_FILE)
  with open(CONFIG_FILE, 'w') as f:
    f.write(SECRET_KEY)

if len(sys.argv) > 1:
  # Consider the entire command line arguments as the task to add
  task = ' '.join(sys.argv[1:])

  # These tasks take longer, so show a "progress" bar
  pdot()
  from todoist import TodoistAPI
  pdot()
  api = TodoistAPI(SECRET_KEY)
  pdot()
  retval = api.quick.add(task)
  pdot()

  # Quick add may "eat" some of the task, but not all
  # For example #myproject becomes a projectid field
  if retval and 'content' in retval.keys() and retval['content'] in task:
    print("OK", end='')
  else:
    print("Error!")
    pprint(retval)
else:
  print("Todoist Quick Add Task, jeffgreenca 2018\n")
  print("Usage: %s <task in quick add syntax>\n" % sys.argv[0])
  print("Example:")
  print("  %s remember to get milk tomorrow #errands @walking p1" % sys.argv[0])
  print("\nExpects Todoist API token in ~/.todoist (or prompts to create it)")
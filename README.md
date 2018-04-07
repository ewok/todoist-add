# todoist-add
Quick-add Todoist tasks from the command line.

## Usage:
```
td plant summer tomatoes @home #hobbies in two weeks
```

Example:
![Screenshot of running the usage command in a Command Prompt window](https://github.com/jeffgreenca/todoist-add/raw/master/examples/example1.png)

Result:
![Screenshot of Todoist UI showing the added task](https://github.com/jeffgreenca/todoist-add/raw/master/examples/example2.png)


See Todoist's [Quick Add syntax](https://support.todoist.com/hc/en-us/articles/115001745265) for details.

*Note - it completely ignores flags, to give you a direct pipe to your Todoist.  Passing flags like --help will create a Todoist task "--help".  That's a feature, not a bug!*

## Installing
On Windows, download [the executable](https://github.com/jeffgreenca/todoist-add/raw/master/dist/td.exe) and place it in your PATH.  Other platforms, alias the Python script or follow the build instructions for a binary.

The first time you run the app, it will ask you for your API token.  Get this from Todoist by going to `Settings -> Integrations -> API token`.

## Building
If you need to build your own binary, and you have Python3 + pipenv installed, you can do this:

```
pipenv install --dev
pipenv run pyinstaller --onefile td.py
```

## Why, when there are better CLIs for Todoist?
It does just one thing.  Invocation is quick and memorable.  The web-based Todoist GUI is wonderful, but sometimes I don't want to switch away from whichever terminal just to add a task that comes to mind.
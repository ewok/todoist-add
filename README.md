# todoist-add
Quick Add Todoist tasks, from the command line.

## Usage:
```
$td <task>
```

For example, to add a task `plant summer tomatoes`, tag it with the label `@home`, assign it to the `#hobbies` project, and set the due date two weeks from now:
```
$td plant summer tomatoes @home #hobbies in two weeks
```

#### Visual Example
![Screenshot of running the usage command in a Command Prompt window](https://github.com/jeffgreenca/todoist-add/raw/master/examples/example1.png)

#### Result
![Screenshot of Todoist UI showing the added task](https://github.com/jeffgreenca/todoist-add/raw/master/examples/example2.png)


See Todoist's [Quick Add syntax](https://support.todoist.com/hc/en-us/articles/115001745265) for details.

*Note - it completely ignores flags, to give you a direct pipe to your Todoist.
As a result, `td --help me obi` will create a Todoist task including the --help.
That's a feature, not a bug ;)*

## Installing
On Windows, download [the executable](https://github.com/jeffgreenca/todoist-add/raw/master/dist/td.exe) and place it in your PATH.  Otherwise, alias the `td.py` script or build your own.

The first time you run the app, it will ask you for your Todoist API token.  Obtain your personal token by logging in to your Todoist account and navigating to `Settings -> Integrations -> API token`.

*Note - the app stores your token in a file under your user profile directory, `~/.todoist`.  Consider if this is sufficiently secure for your computing environment.

## Building
If you need to build your own binary, and you have Python 3 + `pipenv` installed, you can do this:

```
pipenv install --dev
pipenv run pyinstaller --onefile td.py
```

## Why, when there are better CLIs for Todoist?
It does just one thing.  Invocation is quick and memorable.  The web-based Todoist GUI is wonderful, but sometimes I don't want to switch away from whichever terminal just to add a task that comes to mind.

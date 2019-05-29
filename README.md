# todoist-add
Quick Add Todoist tasks, from the command line.

## Usage:
```
$ td <task>
```

For example, to add a task `plant summer tomatoes`, tag it with the label
`@home`, assign it to the `#hobbies` project, and set the due date two weeks
from now:

```
$ td plant summer tomatoes @home #hobbies in two weeks
```

> See Todoist's [Task Quick Add syntax](https://support.todoist.com/hc/en-us/articles/115001745265)

#### Visual Example
![Screenshot of running the usage command in a Command Prompt window](./screenshots/example1.png)

#### Result
![Screenshot of Todoist UI showing the added task](./screenshots/example2.png)

## Installation

### Building from source
Build an executable and place it in your path.
To build an executable, with `pipenv` and Python 3.x, run:

```
pipenv install --dev
pipenv run pyinstaller --onefile td.py
```
### Installing from AUR

#### AUR helper
You can make use of an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers):

    $ yay -S todoist-add-git

#### Manual build
To build and install the package manually:

    $ curl https://aur.archlinux.org/cgit/aur.git/snapshot/todoist-add-git.tar.gz | tar zxf -
    $ cd todoist-add-git
    $ makepkg -si


## Why?

> Probably just use this instead: [sachaos/todoist](https://github.com/sachaos/todoist)

However, if you insist, here are two justifications:

- It does just one thing (is this called "distraction-free"?)
- Invoking is quick and memorable

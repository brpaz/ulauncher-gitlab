# Ulauncher GitLab

> Ulauncher extension to interact with [GitLab](https://gitlab.com/).

## Demo

![demo](demo.gif)

## Features

* Search public projects
* Search your starred projects
* Search your private Projects.
* Search your Groups
* Provides quick access to common GitLab pages like your Issues, Todos and Merge Requests.
* Shortcuts for Gitlab.com and GitLab status page.
* Supports both hosted GitLab.com and On-Premise.

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python-Gitlab package (```pip install python-gitlab```)
* A [GitLab](https://gitlab.com) account and a [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) with **api** scope.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```<%= https://github.com/brpaz/ulauncher-gitlab %>```

## Usage

Before using the extension, you must configure your GitLab access token in the plugin settings.

## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT

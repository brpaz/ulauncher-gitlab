# Ulauncher GitLab

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-gitlab)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-gitlab.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-gitlab)
![License](https://img.shields.io/github/license/brpaz/ulauncher-gitlab.svg?style=for-the-badge)

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

* [ulauncher](https://ulauncher.io/) V5
* Python 3 with the following packages:
  * python-gitlab
* A [GitLab](https://gitlab.com) account and a [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) with **api** scope.


## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```<%= https://github.com/brpaz/ulauncher-gitlab %>```

## Usage

Before using the extension, you must configure your GitLab access token in the plugin settings. You can yours [here](https://gitlab.com/profile/personal_access_token).

## Development

```
make link
make dev
```

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.

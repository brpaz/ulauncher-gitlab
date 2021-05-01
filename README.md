# Ulauncher GitLab

> Ulauncher extension to interact with [GitLab](https://gitlab.com/).

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-gitlab/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-gitlab)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-gitlab.svg?style=for-the-badge)](LICENSE)


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
* A [GitLab](https://gitlab.com) account and a [personal access token](https://gitlab.com/profile/personal_access_token)

## Install

First install all the Python depdendencies needed by this extension:

```sh
sudo apt install python3-pip
pip3 install "python-gitlab >=1.5.1,<2.0.0"
```

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```<%= https://github.com/brpaz/ulauncher-gitlab %>```

## Usage

Before using the extension, you must configure your GitLab access token in the plugin settings. You can yours [here](https://gitlab.com/-/profile/personal_access_tokens).

## Development

```
make link
make dev
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)


Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.

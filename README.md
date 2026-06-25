# QA Automation using BrowserStack, Selenium (Python) and GitHub Actions

> **Note**: This project is a modified and hopefully better version of a [tutorial/article](https://cuimri.com/posts/test-automation-selenium/) I wrote in late 2022 for my technical writing interview at BrowserStack.

A testing workflow made with Python, Selenium, and automated parallel testing across heterogeneous browser landscapes via BrowserStack and CI/CD pipelines via GitHub Actions.

## Setup Instructions
1. Run `bash set_up.sh` to initialize your local Python environments.
2. Duplicate `.env.example` as `.env` and fill in your unique platform keys.
3. Launch local execution through `python local_script.py` or run remote parallel sessions with `python browserstack_script.py`.

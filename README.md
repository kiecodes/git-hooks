# How to use git hooks

Hello. Thank you for being here. This repository belongs to the youtube video [How to use GIT HOOKS for better COMMITS](https://youtu.be/EvpZkdkp-v0).
If you haven't seen it, please consider watching the video, to get a better understanding of this code.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/EvpZkdkp-v0/0.jpg)](https://www.youtube.com/watch?v=EvpZkdkp-v0))

## Content

The following files are included:
|File| Description |
|--|--|
| commit-msg.py | A commit-msg git-hook implementation to check the commit message for 5 of the 7 rules for a proper commit message (see below) with a Philips Hue integration. |
| install_hooks.sh | A shell script to install the hook into this repository to try it out. 
| requirements.txt | Python library requirements to use with pip.

## How to use this hook

If you just want to play around with this project you can run the install_hooks.sh script to install this hook in your local clone of this repository and try out some commits. Make sure that you add your Hue Bridge IP and Hue Lamp Name to the commit-msg.py script as well.

The Philips Hue integration is not fail-safe, so I added a switch to activate the indication as soon as all necessary information
is provided. If you want to use the Phillips Hie integration set HUE_ACTIVE to true after you defined your bridge's IP address and lamp name.

If you plan to use this in another repo, you can copy the hook scripts and the install_hooks.sh to it and check it distribute it to your teammates. Make sure to also add a little paragraph to your README.md, to let them know about the new hooks.

## Requirements

The commit-msg.py hook uses the phue library. Please click [here](https://github.com/studioimaginaire/phue) for more details.

## Seven rules for a great commit message

 - Separate subject from the body with a blank line.
 - Limit the subject line to 50 characters.
 - Capitalize the subject line.
 - Do not end the subject line with a period.
 - Use the imperative mood in the subject line.
 - Wrap the body at 72 characters.
 - Use the body to explain what and why vs. how.

## Contribution
New ideas for hooks are always welcome. Please fork and create a pull request if you have some creative additions.
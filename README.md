# Wunderground Pushover script
===============================

A script to send wunderground rss data to pushover

## Requirements
================
* Pushover account created via https://pushover.net
* Pushover device client installed and setup with your account
* Python installed

## Installation and Setup
==========================
### Pushover setup
* Go to your Pushover account and create a new script application

### Script setup
1. Clone the repo locally
2. Open localconfig.py
3. Add your app's API token
4. Add your user key
5. Update the RSS url and link url for Wunderground to be your weather
6. Save the file

## Testing
===========
At this point, you're all setup.  Try running `python wunderground-pushover.py` and you should get notified with today's weather.


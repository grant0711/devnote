# devnote

Local python application and remote Django REST api server to record and store my personal developer notes.


## Description

This application solves the problem of easily capturing and storing my personal developer notes on the cloud. Over the years I've tried a number of solutions, including Google Docs, Google Keep, Jupyter Notebooks, and editing local files- none of which were very sticky for me and enabled me to effortlessly take notes on the fly as I'm working through a new tool or language. The main problem with all of these tools is that they require toggling between active windows. As part of my workflow, I try to avoid toggling as much as possible to maintain focus on a limited number of things while engaging in deep work. Thus, my habit of taking detailed developer notes became weak over time, and the final result is that by the time I'm finished learning a new tool, I've left no trace of the specific detailed steps I took to get there.

Devnote addresses this problem by creating a very simple user flow where I may open up and append my notes to an existing local file via the command line. After each addition to my local devnote, the content of the note is automatically posted to a server that receives and updates a record for that note in a database. Thus, while taking notes on the fly I can simply type my notes into the command line little by little, and the syncing with my server is taken care of automatically. When I wish to review my notes, I can do so via the UI of my webserver, or via downloading devnotes locally on my machine.

These notes may then be consulted periodically to review previous work in case of troubleshooting, or in the crafting of detailed documentation that comes after a significant development push. They are not meant to be clean as recorded. The overall goal is to increase long-term productivity by promoting the ability to learn once and only once, and gradually improve documentation quality over time.

## Setup

Only works with linux with python3

#### Local Setup:

```
git clone git@github.com:grant0711/devnote.git
cd devnote/

bash install.sh
```

This will ask you to input the url of the POST endpoint where your devnotes will be sent, your user token and to specify the local folder where your local devnotes will be stored. These will be written as environmental variable exports to your .bashrc file.

#### Server Setup:

TBD


#### Local Development:

The webserver can be deployed locally via docker and docker-compose:

```
docker-compose build api_dev
docker-compose up api_dev
```

Out of the box your web server will be available on localhost at port 8000, and your postgres instance available on port 5000. Note that currently the database volume does not persist, so you will need to run migrations and create any superuser/user required to interact locally. This may be accomplished after bringing up api_dev and database docker containers in a different terminal:

```
docker-compose run api_dev python3 manage.py migrate
docker-compose run api_dev python3 manage.py createsuperuser
```

After creating a superuser navigate to 127.0.0.1:8000/admin and create a new user and user token.


To just run tests with pytest watch:

```
docker-compose build api_test
docker-compose up api_test
```

## Tasks

DONE:
- Create local executable and install script to capture notes via command line in local file
- Add to executable ability to post notes to an api
- Add django project and apps
- Add initial tests and set up CI
- Add admin portal and setup static

TODO:
- Create users and setup token authentication
- Create models for inbound events (devnotes)
- Add endpoints to receive inbound events (devnote upserts)
- Choose deployment platform
- Add terraform and automate deployment
- Add method to query devnotes from the server given a date range and create combined devnote file within local folder
- Configure admin portal to render notes searchable via web ui
- Create a front end to search for and display devnotes to users via web ui

# devnote

Local python application and remote Django REST api server to record and store my personal developer notes.


## Description

This application solves the problem of easily capturing and storing my personal developer notes on the cloud. Over the years I've tried a number of solutions, including Google Docs, Google Keep, Jupyter Notebooks, and editing local files- none of which were very sticky for me and enabled me to effortlessly take notes on the fly as I'm working through a new tool or language. The main problem with all of these tools is that they require toggling between active windows. As part of my workflow, I try to avoid toggling as much as possible to maintain focus on a limited number of things while engaging in deep work. Thus, my habit of taking detailed developer notes became weak over time, and the final result is that by the time I'm finished learning a new tool, I've left no trace of the specific detailed steps I took to get there.

Devnote addresses this problem by creating a very simple user flow where I may open up and append my notes to an existing local file via the command line. After each addition to my local devnote, the content of the note is automatically posted to a server that receives and updates a record for that note in a database. Thus, while taking notes on the fly I can simply type my notes into the command line little by little, and the syncing with my server is taken care of automatically. When I wish to review my notes, I can do so via the UI of my webserver, or via downloading devnotes locally on my machine.

## TODOs

- Create users and setup token authentication
- Create models for inbound events (devnotes)
- Add endpoints to receive inbound events (devnote upserts)
- Add terraform and heroku deploy to a pipeline
- Add method to query devnotes from the server given a date range and create combined devnote file within local folder
- Configure admin portal to render notes searchable via web ui
- Create a front end to search for and display devnotes to users via web ui

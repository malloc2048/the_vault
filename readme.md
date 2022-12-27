# Vault
Welcome to The Vault a place where random stuff is catalogued.

## Development Notes
An attempt was made to make this as simple as possible, epsecialy when adding new models 

### Adding a new model
To add a new model:
* create a file in `vault/app/models/`
* It is important that the name of the file match the model_type that will be used in data files
  * this name is used to match data in a data file to a model
* In the file instantiate an instance of `Model` providing required parameters
  * `display_name` - this is the name that will appear in the nav bar of the web pages
  * `display_fields` - this is a list of the fields of this data type that will be displayed in tables

## Running the Vault

### Dependencies
* Docker
* Docker Compose

### Linux
* clone the repo 
    * `git clone git@github.com:malloc2048/vault.git`
* build the docker image
  * `docker-compose -f docker-compose-<env>.yaml build`
  * Note: for building it doesn't matter which compose file is specified
* run the container
  * `docker-compose -f docker-compose-<env>.yaml up`

### Windows with WSL 2
TODO

## Project structure
### app
The main code of the application
* api_routes - route definitions for the REST API 
* config - application and gunicorn configuration files
* models - data models for items stored in the database
* templates - HTML templates for web page
* routes.py - web page route definitions
* utils.py - some utility functions

### scripts
Some helper scripts
* add_data.py - a python script to add data to the database through the API
* start.sh - script used in docker container to run the gunicorn server

### docker-compose-dev.yaml
Development docker compose file that maps repo code directories in running container.  
Using this file, changes made to source files are reflected in the running container without restarting it
Maps port 8001 in the container to port 80 on the host so application can be accessed from http://localhost

### docker-compose-prod.yaml
Production docker compose file.  
Maps port 8001 in the container to port 80 on the host so application can be accessed from http://localhost

### Dockerfile
Dockerfile used to build the image containing all needed components to run the Vault

### requirements.txt
Python package requirements file 

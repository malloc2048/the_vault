# Vault 81
Welcome to Vault 81 a place where random stuff is catalogued.

## Running the Vault

### Dependencies
* Docker
* Docker Compose

### Linux
* clone the repo 
    * `git clone git@github.com:malloc2048/vault81.git`
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

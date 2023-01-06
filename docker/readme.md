# Docker Files
These files are used to buld and run the Vault docker image/container

## docker-compose-dev.yaml
Docker compose file to run a development version of the Vault container.  
This compose file will map the Vault source files in the repository to the running container making development easier

## docker-compose-prod.yaml
Docker compose file to run a production version of the Vault container

## Dockerfile
Main dockerfile to build the Vault docker image

## requirements.txt
Paython package requirements installed during image build

## start.sh
This script is used in the container to start the gunicorn web server to serve the Vault application

FROM ubuntu:22.04 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Copy the application code and fix file ownership.
COPY ./app /my_stuff/app
COPY requirements.txt /my_stuff
COPY scripts/start.sh /my_stuff/scripts/start.sh
WORKDIR /my_stuff

# install python
RUN apt-get update && apt-get install -y python3-dev python3-pip python3-venv

# install python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=/mystuff/app
ENV FLASK_DEBUG=True
ENV PYTHONPATH=/my_stuff

CMD [ "/my_stuff/scripts/start.sh" ]

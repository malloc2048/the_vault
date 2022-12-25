FROM ubuntu:22.04 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Copy the application code and fix file ownership.
COPY ./app /vault81/app
COPY requirements.txt /vault81
COPY scripts/start.sh /vault81/scripts/start.sh
WORKDIR /vault81

# install python
RUN apt-get update && apt-get install -y python3-dev python3-pip

# install python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=/vault81/app
ENV FLASK_DEBUG=True
ENV PYTHONPATH=/vault81

CMD [ "/vault81/scripts/start.sh" ]

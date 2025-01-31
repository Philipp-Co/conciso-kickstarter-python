from python:alpine3.21

COPY docker/start.sh /docker/start.sh
RUN chmod +x /docker/start.sh
COPY requirements/production.txt /requirements/production.txt
RUN pip install -r /requirements/production.txt
COPY kickstarter/ /kickstarter/

WORKDIR /kickstarter/

ENTRYPOINT /docker/start.sh /kickstarter/

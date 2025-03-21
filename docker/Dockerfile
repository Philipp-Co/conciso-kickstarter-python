from python:alpine3.21

COPY docker/start.sh /docker/start.sh
RUN chmod +x /docker/start.sh
COPY requirements/production.txt /requirements/production.txt
RUN pip install -r /requirements/production.txt
COPY kickstarter_business_logic/ /kickstarter_business_logic/
RUN pip install build && cd /kickstarter_business_logic/ && python -m build --sdist && cd dist && pip install kickstarter_business_logic-0.0.1.tar.gz && cd /
COPY kickstarter/ /kickstarter/

WORKDIR /kickstarter/

ENTRYPOINT /docker/start.sh /kickstarter/

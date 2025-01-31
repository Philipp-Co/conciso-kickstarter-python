# Python Kickstarter

Aufbau eines Template Projekts in Python.
todo...

# Entwicklungsumgebung

## Style Guide

    https://google.github.io/styleguide/pyguide.html

## Virtuelle Umgebung

    // Eine virtuelle Umgebung fuer Python erstellen und aktivieren.
    python -m venv venv
    source venv/bin/activate

    // pruefen, ob die Systempfade richtig gesetzt sind.
    // which python -> /Users/mustermann/Repositories/conciso-python-kickstarter/venv/bin/python

    // Packete installieren.
    pip install -r requirements/develop.txt

    // Packetliste pruefen
    pip freeze

## pre-commit

    // pre-commit Hooks installieren
    pre-commit install -t pre-commit

Uebder die Konfigurationsdatei .pre-commit-config.yaml kann das Verhalten von pre-commit angepasst werden.
Mit

    pre-commit run --all-files

koennen die Dateien im Projekt geprueft werden.

## django

    https://docs.djangoproject.com/en/5.1/intro/tutorial01/

## Anwendung starten und Verwenden

Die Anwendung direkt im Terminal starten:

    // in kickstarter/
    ./manage.py runserver 0.0.0.0:8000 --settings kickstarter.settings

Die Anwendung über Docker-Compose starten:
Zunaechst sollte die Anwendung gebaut werden

    // Docker Image bauen
    docker-compose build kickstarter

    docker image ls | grep kickstarter
    // Gibt beispielhaafte Ausgebe
    kickstarter                    latest                  7d8afcecb8c8   5 minutes ago    109MB

    // Docker Umgebung starten
    docker-compose up kickstarter

Den Endpunkt aufrufen...
... um alle bekanten Personen zu Listen

    curl -XGET http://localhost:8000/persons/

... um eine Person anzulegen

    curl -XPOST http://localhost:8000/persons/ -d '{"name": "Max", "surname": "Mustermann"}'

## OpenAPI - openapi.yaml generieren

Die Anwendung hat eine durch Spectacular dokumentierte REST-API. Die Dokumentation kann ich From einer openapi.yaml generiert werden.

    // Die Anwendung wurde im Terminal gestartet
    ./manage.py spectacular --color --file=./openapi.yaml

    // Die Anwendung wird in der Docker-Compose Umgebung ausgefuehrt
    ../docker/export-openapi.sh
    // Nach Aufruf liegt die open-api.yaml Datei unter docker/exchange/openapi.yaml

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

    curl -XGET http://localhost:8000/person/

... um eine Person anzulegen

    curl -XPOST http://localhost:8000/person/ -d '{"name": "Max", "surname": "Mustermann"}'

## OpenAPI - openapi.yaml generieren

Die Anwendung hat eine durch Spectacular dokumentierte REST-API. Die Dokumentation kann ich From einer openapi.yaml generiert werden.

    // Die Anwendung wurde im Terminal gestartet
    ./manage.py spectacular --color --file=./openapi.yaml

    // Die Anwendung wird in der Docker-Compose Umgebung ausgefuehrt
    ../docker/export-openapi.sh
    // Nach Aufruf liegt die open-api.yaml Datei unter docker/exchange/openapi.yaml

## Keycloak
Um den Keycloak aufzusetzten muss er ueber docker-compose gestartet und ueber die Weboberflaeche eingerichtet werden.
Der Zustand wird unter docker/keycloak/data/import/skillprfil.json gespeicher und bei jedem Neustart importiert.
Folgendes Kommando speichert den aktuellen Zustand:

    docker exec -it iam sh -c "/opt/keycloak/bin/kc.sh export --realm skillprofil --file /opt/keycloak/data/import/skillprofil-realm.json"

In der vorliegenden Konfiguration gibt es einen Benutzer den der Keycloak kennt, dieser Benutzer heisst

    Name: Thorin 
    Nachname: Eisenbart
    Username: hrm
    Password: Eisenbart

Thorin Eisenbart hat die Rolle "Human Ressource Manager" inne mit der er in der Anwendung unbekannte Personen anheuern darf.

### Einen Access Token holen

    curl -XPOST http://localhost:8080/realms/skillprofil/protocol/openid-connect/token -k -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=hrm&password=Eisenbart&grant_type=password&client_id=skillprofil-client'
    

### Einen abgesicherten Endpunkt aufrufen   
Der Endpunkt kann mit folgendem Request aufgerufen werden
 
    curl -XPOST http://localhost:8000/person/ -H "Authorization: Bearer $(curl -XPOST http://localhost:8080/realms/skillprofil/protocol/openid-connect/token -k -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=hrm&password=Eisenbart&grant_type=password&client_id=skillprofil-client' | jq -r '.access_token')" -d '{"name": "Kragin", "surname": "Kupferhelm"}'



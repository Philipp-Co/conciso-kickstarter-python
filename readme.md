# Python Kickstarter

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

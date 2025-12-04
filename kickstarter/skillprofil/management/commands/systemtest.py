"""Systemtest Command."""

# ---------------------------------------------------------------------------------------------------------------------
from argparse import ArgumentParser
from unittest import TestResult, TextTestRunner, defaultTestLoader

from django.core.management import BaseCommand, CommandError

# ---------------------------------------------------------------------------------------------------------------------


class Command(BaseCommand):
    """Systemtest Command."""

    def __init__(self):
        """C'tor."""
        super().__init__()
        self.help = 'Mit diesem Kommando wird ein Systemtest durchgefuehrt.'
        pass

    def add_arguments(self, parser: ArgumentParser) -> None:
        """Add additional Arguments needed for testing here."""
        pass

    def handle(self, *args, **kwargs) -> None:
        """Djangos Commandhandler.

        This Method will be called when manage.py is executed with "systemtest" as its first argument.
        """
        runner: TextTestRunner = TextTestRunner(
            verbosity=kwargs['verbosity'],
        )
        result: TestResult = runner.run(
            defaultTestLoader.discover(
                start_dir='skillprofil.tests.systemtest',
                pattern='test_*.py',
                top_level_dir='.',
            )
        )

        if not result.wasSuccessful():
            raise CommandError('The Test was not successful...')

        pass

    pass


# ---------------------------------------------------------------------------------------------------------------------

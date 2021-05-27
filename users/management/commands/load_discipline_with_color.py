"""Import disciplines to Datababse."""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from users.models import Discipline

User = get_user_model()

DISCIPLINES = {
    "iqfoil": {"title": "iQFOiL", "slug": "iqfoil", "color": "orange"},
    "openfoil": {"title": "Open Foil", "slug": "openfoil", "color": "green"},
    # "formula": {"title": "Formula", "slug": "formula", "color": "purple"},
}


class Command(BaseCommand):
    def import_disciplines(self):
        for discipline in DISCIPLINES:
            try:
                discipline, created = Discipline.objects.get_or_create(
                    title=DISCIPLINES[discipline]["title"],
                    slug=DISCIPLINES[discipline]["slug"],
                    color=DISCIPLINES[discipline]["color"],
                )
                if created:
                    discipline.save()
                    display_format = "Discipline, {}, has been saved."
                    print(display_format.format(discipline))
                else:
                    print(f"Discipline -{discipline}- already exists")
            except Exception as ex:
                print(str(ex))
                msg = "\n\nSomething went wrong saving this discipline: "
                "{}\n{}".format(discipline, str(ex))
                print(msg)

    def handle(self, *args, **options):
        """Call the function to import data."""
        self.import_disciplines()

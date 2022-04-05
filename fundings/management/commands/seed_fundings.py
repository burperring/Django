from django.core.management.base import BaseCommand
from django_seed import Seed
from fundings import models as funding_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command create many fundings"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many fundings you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(funding_models.Funding, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} fundings created!"))

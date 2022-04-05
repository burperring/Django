import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
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
        seeder.add_entity(
            funding_models.Funding,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "guests": lambda x: random.randint(1, 10),
                "price": lambda x: random.randint(100, 2000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = funding_models.Amenity.objects.all()
        facilities = funding_models.Facility.objects.all()
        rules = funding_models.HouseRule.objects.all()
        for pk in created_clean:
            funding = funding_models.Funding.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                funding_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    funding=funding,
                    file=f"funding_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    funding.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    funding.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    funding.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} fundings created!"))

import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from musics import models as music_models


class Command(BaseCommand):

    help = "This command create review"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        musics = music_models.Music.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "critic_score": lambda x: random.randint(2, 5),
                "user_score": lambda x: random.randint(2, 5),
                "user": lambda x: random.choice(users),
                "music": lambda x: random.choice(musics),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} review created!"))

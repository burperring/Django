import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from musics import models as music_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command create many musics"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many musics you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            music_models.Music,
            number,
            {
                "name": lambda x: seeder.faker.name(),
                "lyricist": lambda x: random.choice(all_users),
                "price": lambda x: random.randint(100, 2000),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            music = music_models.Music.objects.get(pk=pk)
            for i in range(1, random.randint(3, 5)):
                music_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    music=music,
                    file=f"music_photos/{random.randint(1, 31)}.jpg",
                )
        self.stdout.write(self.style.SUCCESS(f"{number} musics created!"))

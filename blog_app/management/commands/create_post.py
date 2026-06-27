from django.core.management.base import BaseCommand

from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--title', type=str)
        parser.add_argument('--content', type=str)
    def handle(self, *args, **options):
        try:
            post = Post.objects.create(title=options['title'], content=options['content'])
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Ошибка при добавлении статьи - {e}'))
            return
        self.stdout.write(self.style.SUCCESS(f'Статья {post.id} - {post.title} успешно добавлена'))

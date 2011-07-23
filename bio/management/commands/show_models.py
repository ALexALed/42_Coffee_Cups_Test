__author__ = 'alexaled'


from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This command print all models and count their elements'

    def handle(self, *args, **options):

        from django.db.models import get_models

        result_list = []
        for model in get_models():
            result_list.append('[%s] - %s objects' % (model.__name__,
                                        model._default_manager.count()))
            return '\n'.join(result_list)

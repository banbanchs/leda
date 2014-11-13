# coding=utf-8

from django.core.management import BaseCommand

from api.crawler import run


class Command(BaseCommand):
    def handle(self, *args, **options):
        if args:
            run(int(args[0]))
        else:
            run()

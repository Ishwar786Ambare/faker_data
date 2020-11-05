import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cronjob.settings')
import django

django.setup()

from cronjobapp.models import DataTable
from faker import Faker
from random import *

faker = Faker()


def main(n):
    for i in range(n):
        num = randint(1001, 9999)
        name = faker.name()
        data_red = DataTable.objects.get_or_create(name=name, number=num)


main(1000)

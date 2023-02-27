from home.models import Names
from faker import Faker
fake = Faker()



def seeddb(n):
    for i in range(0,n):
        Names.objects.create(
            name=fake.name()
        )

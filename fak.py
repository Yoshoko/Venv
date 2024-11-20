from faker import Faker

fake = Faker("fr_FR")

for _ in range(10):
    print(fake.name())
    print(fake.job())
    print(fake.company())
    print(fake.date_this_month().isoformat())
    print(fake.url())
    print("-"*10)


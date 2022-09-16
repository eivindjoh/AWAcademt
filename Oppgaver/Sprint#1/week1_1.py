import random

health = 100
health_potion = 10

health -= random.randint(20, 30)
health -= random.randint(20, 30)
health += (health_potion + random.randint(10, 15))
print(health)

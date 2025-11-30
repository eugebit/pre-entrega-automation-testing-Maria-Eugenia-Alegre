from django.contrib.auth import login
from django.template.defaultfilters import length
from faker import Faker

fake = Faker()


def get_login_faker(num_casos=5):
    casos = []
    usuarios_validos = ["visual_user", "standard_user"]
    password_valido = "secret_sauce"
    for _ in range(num_casos):
        if fake.boolean(chance_of_getting_true=50):
            username = fake.random_element(elements=usuarios_validos)
            password = password_valido
            login_example = True
        else:
            username = fake.user_name()
            password = fake.password(length=12)
            login_example = False

        casos.append((username, password, login_example))

    return casos

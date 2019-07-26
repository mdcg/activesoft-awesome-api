from django.contrib.auth.models import User

from api.tests.testingutils.generators.data_generators import UserDataGenerator


def create_user():
    user_generator = UserDataGenerator()

    user = User.objects.create(
        first_name=user_generator.get_first_name(),
        last_name=user_generator.get_last_name(),
        username=user_generator.generate_username(),
        email=user_generator.generate_email()
    )
    user.set_password('123456')
    user.save()

    return user

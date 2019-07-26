import random

NAMES = [
    'Coralie Altschuler',
    'Carola Barrientos',
    'Kyle Maggi',
    'Lino Gooden',
    'Ronda Murakami',
    'Pearle Palombo',
    'Woodrow Dearborn',
    'Gisela Mccaul',
    'Ashly Lebeau',
    'Seymour Litchfield',
]


class UserDataGenerator(object):
    def __init__(self):
        self._name = self.__generate_random_name()

    def __generate_random_name(self):
        return random.choice(NAMES)

    def get_fullname(self):
        return self._name

    def get_first_name(self):
        return self._name.split(' ')[0]

    def get_last_name(self):
        return self._name.split(' ')[1]

    def generate_email(self):
        return f'{self.generate_username()}@activesoft.com'

    def generate_username(self):
        return self.__concatenate_name(self.__lowercase_name(self._name))

    def __concatenate_name(self, name):
        return ''.join(name.split())

    def __lowercase_name(self, name):
        return name.lower()

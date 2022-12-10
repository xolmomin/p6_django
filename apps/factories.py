import factory


class UserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = "John"
    lastname = "Doe"

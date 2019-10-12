# -*- encoding: utf-8 -*-

import factory
from faker import Factory as FakerFactory

from example.models import (
    Author,
    Blog,
)

faker = FakerFactory.create()
faker.seed(883843)


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyAttribute(lambda x: faker.name())
    content = factory.LazyAttribute(lambda x: faker.name())

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
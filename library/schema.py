import graphene
from graphene_django import DjangoObjectType
from library import models

"""Creating types"""

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author

class BookType(DjangoObjectType):
    class Meta:
        model = models.Book

"""Bringing types together and making querable"""

class Query(graphene.ObjectType):
    autors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    books_by_author = graphene.List(BookType, author_family_name = graphene.String())

    def resolve_authors(self, info):
        return models.Author.objects.all()
    def resolve_books(self, info):
        return models.Book.objects.all()
    def resolve_books_by_author(self, info, author_family_name):
        return models.Book.objects.filter(
            author__family_name=author_family_name,
        )
schema = graphene.Schema(query=Query)
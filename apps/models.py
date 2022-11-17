# from django.db import models
# from django.db.models import (
#     Model,
#     CharField,
#     ForeignKey,
#     CASCADE, TextChoices
# )
#
#
# class Region(Model):
#     # OLD = 'OLD'
#     # NEW = 'NEW'
#     # STATUS = (
#     #     (OLD, 'eski'),
#     #     (NEW, 'yangi'),
#     # )
#     # class StatusChoice(TextChoices):
#     #     OLD = 'OLD', 'eski viloyatlar'
#     #     NEW = 'NEW', 'yangi viloyatlar'
#
#     # name = CharField(max_length=255, unique=True, blank=True, null=True, choices=STATUS, default=OLD)
#     # name = CharField(max_length=255, blank=True, null=True, choices=StatusChoice.choices, default=StatusChoice.OLD)
#     name = CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class District(Model):
#     owner = CharField(max_length=255, null=True)
#     state = CharField(max_length=255)
#     name = CharField(max_length=255)
#     region = ForeignKey('apps.Region', CASCADE)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Hero(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     benevolence_factor = models.PositiveSmallIntegerField(
#         help_text="How benevolent this hero is?",
#         default=50
#     )
#
#     def __str__(self):
#         return self.name
from django.db.models import Model, CharField, TextField, DateTimeField, ImageField


class Blog(Model):
    name = CharField(max_length=255)
    description = TextField()
    picture = ImageField(upload_to='blogs/', default='blogs/default.png')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Region(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

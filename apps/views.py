# from django.contrib.admin.models import LogEntry
# from django.contrib.auth.models import User, Group
# from django.db.models import Subquery, OuterRef
# from django.shortcuts import render
#
# from apps.models import Region, District, Hero, Category
#
# '''
# changepassword
# startapp
# runserver
# makemigrations
# migrate
# createsuperuser
# shell
# dbshell
# '''
#
# def main_page(request):
#     # region = Region.objects.first()
#     # region.name = 'New Tashkent'
#     hero_qs = Hero.objects.filter(
#         category=OuterRef("pk")
#     ).order_by("-benevolence_factor")
#     Category.objects.all().annotate(
#         most_benevolent_hero=Subquery(
#             hero_qs.values('name')[:1]
#         )
#     )
#
#     District.objects.filter(region__name__startswith='Tosh')
#     District.objects.filter()
#     # region.save()
#     # JsonField
#     # a = student
#     # User.objects.values_list('username', flat=True)
#     return render(request, 'apps/index.html')
# # auth_user
# # appnomi_modelnomi
#
#
# # models, django-orm, mysql, postgres, mongodb
#
#
from django.shortcuts import render

from apps.models import Blog


def main_page(request):
    return render(request, '')


def blog_page(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'apps/blog-page.html', context)


def add_blog_page(request):
    if request.method == 'POST':
        Blog.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )

    return render(request, 'apps/add-blog.html')


'''
https://books.agiliq.com/projects/django-orm-cookbook/en/latest/index.html# (gruppada rasmi bor)
https://books.agiliq.com/projects/django-admin-cookbook/en/latest/ (hammasi)

https://docs.djangoproject.com/en/4.1/ref/models/fields/ (hamma fields)
https://python101.pythonlibrary.org/index.html# (20gacha)



'''

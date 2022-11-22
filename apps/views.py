from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.forms import LoginForm
from apps.models import User


class IndexView(TemplateView):
    template_name = 'apps/index.html'


class RegisterView(TemplateView):
    template_name = 'apps/auth/register.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index_view')
    template_name = 'apps/auth/register.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'apps/auth/login.html'
    next_page = reverse_lazy('index_view')

# #
# # def main_page(request):
# #     # region = Region.objects.first()
# #     # region.name = 'New Tashkent'
# #     hero_qs = Hero.objects.filter(
# #         category=OuterRef("pk")
# #     ).order_by("-benevolence_factor")
# #     Category.objects.all().annotate(
# #         most_benevolent_hero=Subquery(
# #             hero_qs.values('name')[:1]
# #         )
# #     )
# #
# #     District.objects.filter(region__name__startswith='Tosh')
# #     District.objects.filter()
# #     # region.save()
# #     # JsonField
# #     # a = student
# #     # User.objects.values_list('username', flat=True)
# #     return render(request, 'apps/index.html')
# # # auth_user
# # # appnomi_modelnomi
# #
# #
# # # models, django-orm, mysql, postgres, mongodb
# #
# #
# from django.shortcuts import render
#
# from apps.models import Blog
#
#
# def main_page(request):
#     return render(request, 'apps/index.html')
#
#
# def blog_page(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs': blogs
#     }
#     return render(request, 'apps/blog-page.html', context)
#
#
# def add_blog_page(request):
#     if request.method == 'POST':
#         Blog.objects.create(
#             name=request.POST.get('name'),
#             description=request.POST.get('description')
#         )
#
#     return render(request, 'apps/add-blog.html')
#

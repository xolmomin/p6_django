from django.conf.urls.static import static
from django.urls import path

from apps.views import main_page, blog_page,add_blog_page
from p6_django.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', main_page, name='main_page'),
    path('blog', blog_page, name='blog_page'),
    path('add-blog', add_blog_page, name='add_blog_page'),
] + static(STATIC_URL, document_root=STATIC_ROOT)

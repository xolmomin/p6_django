from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from apps.bot import UpdateBot
from apps.views import IndexView, RegisterView
from root.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('login', LoginView.as_view(
        next_page=reverse_lazy('index_view'),
        template_name='apps/auth/login.html'
    ), name='login'),
    path('logout', LogoutView.as_view(
        next_page=reverse_lazy('index_view')
    ), name='logout'),

    # path('login', CustomLoginView.as_view(), name='login_view'),
    # path('logout', CustomLogoutView.as_view(), name='logout_view'),
    path('register', RegisterView.as_view(), name='register_view'),
    path('bot/', csrf_exempt(UpdateBot.as_view()), name='register_view'),
] + static(STATIC_URL, document_root=STATIC_ROOT)

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from main import views as app_views


urlpatterns = [
    url(r'^$', app_views.home, name='home'),
]

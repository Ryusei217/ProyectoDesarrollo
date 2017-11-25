from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from perfiles.views import PerfilEditarView
from avatar import urls as avatar_urls


urlpatterns = [
    url(r'^avatar/', include(avatar_urls)),
    url(r'^editar/', login_required(PerfilEditarView.as_view()), name='perfil_editar'),
    url(r'^$', login_required(TemplateView.as_view(template_name='perfiles/perfil.html')), name='perfil_home'),
]
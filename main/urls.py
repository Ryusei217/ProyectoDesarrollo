from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from main import views as app_views


urlpatterns = [
    url(r'^$', app_views.home, name='home'),

    # Componentes
    url(r'^componentes/data/$', app_views.ComponenteJson.as_view(), name="componente_data"),
    url(r'^componentes/$', app_views.ComponenteList.as_view(), name="componente_list"),
    url(r'^componentes/create/$', app_views.ComponenteCreate.as_view(), name="componente_create"),
    url(r'^componentes/(?P<pk>\d+)/editar/$', app_views.ComponenteUpdate.as_view(), name="componente_update"),
    url(r'^componentes/eliminar/$', app_views.ComponenteDelete.as_view(), name="componente_delete"),
]

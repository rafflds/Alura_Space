from django.urls import path
# Conectando a pasta galeria, arquivo views, importando função index
from galeria.views import index


urlpatterns = [
    path('', index)
]
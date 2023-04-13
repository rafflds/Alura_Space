from django.contrib import admin
# Importando o path do arquivo url da galeria, incluindo
from django.urls import path, include


# Sequências de URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),  # tendo acesso a pasta galeria, arquivo urls.py (arquivo q eu criei, não vem por padrão)
]

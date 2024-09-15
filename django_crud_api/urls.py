from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tasks.urls')),  # Asegúrate de que la URL esté correcta
    path('docs/', include_docs_urls(title='Task API')),
]

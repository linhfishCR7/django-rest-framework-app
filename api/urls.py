from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/test/', include('tests.urls'), name='test')

]

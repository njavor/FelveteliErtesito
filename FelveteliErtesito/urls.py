from django.contrib import admin
from django.urls import path

from felvetel.views import index, uploadcsvview


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('csv-feltoltes/', uploadcsvview, name='up_csv')
]

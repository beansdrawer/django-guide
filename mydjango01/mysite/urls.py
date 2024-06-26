from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='myapp/', view=include('myapp.urls')),
    path(route='', view=lambda request: redirect('/myapp/')),

]

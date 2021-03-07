from django.urls import path
from . import views
from . import short_view

urlpatterns = [
    path('', views.index),
    path('s/', short_view.short_url),
    # path()
]

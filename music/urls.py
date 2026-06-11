# django
from django.urls import path
from . import views

# music views
#from .views import IndexView


#urlpatterns = [
#    path('', IndexView.as_view()),
#]

urlpatterns = [
    path("", views.index, name='index'),
    path("artist/<artist_id>/", views.artist_detail, name='artist_detail'),
]
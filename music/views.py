# django
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from music.models import Artist


#class IndexView(TemplateView):
#    template_name = "music/index.html"

def index(request):
    return HttpResponse("Bienvenido a la app de Music.")

def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    context = {'artist': artist}
    return render(request, 'music/artist_detail.html', context)
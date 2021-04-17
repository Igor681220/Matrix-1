from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound, Http404
from .Storage import shorts


# Create your views here.

def full_url(request: HttpRequest, key):
    try:
        url = shorts[key]
        return HttpResponseRedirect(url)
    except KeyError:
        raise Http404()

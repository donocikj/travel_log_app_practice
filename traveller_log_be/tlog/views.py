from django.http import HttpResponse

# Create your views here.

def test_view(req):
    return HttpResponse("test view for the tlog")
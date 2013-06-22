from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World!")


def current_datetime(request):
  now = datetime.datetime.now()
  html = "<html><body>The current time is %s.</body></html>" % now
  return HttpResponse(html)

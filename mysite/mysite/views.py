from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World!")


def current_datetime(request):
  now = datetime.datetime.now()
  html = "<html><body>The current time is %s.</body></html>" % now
  return HttpResponse(html)

def time_plus(request, offset):
  try:
    hrs = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=hrs)
  html = "<html><body>The time in %d hours will be %s.</body></html>" % (hrs, dt)
  return HttpResponse(html)


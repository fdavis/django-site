from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World!")


def current_datetime(request):
  now = datetime.datetime.now()
  data = {}
  data['date'] = now
  c = Context(data)
  t = get_template('datetime.html')
  html = t.render(c)
  return HttpResponse(html)

def time_plus(request, offset):
  try:
    hrs = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=hrs)
  html = "<html><body>The time in %d hours will be %s.</body></html>" % (hrs, dt)
  return HttpResponse(html)

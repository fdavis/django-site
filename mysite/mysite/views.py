from django.shortcuts import render
import datetime

def hello(request):
  return HttpResponse("Hello World!")


def current_datetime(request):
  now = datetime.datetime.now()
  data = {}
  data['date'] = now
  data['title'] = 'Current Date'
  return render(request, 'datetime.html', data)

def time_plus(request, offset):
  try:
    hrs = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=hrs)
  html = "<html><body>The time in %d hours will be %s.</body></html>" % (hrs, dt)
  return HttpResponse(html)

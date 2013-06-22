from django.shortcuts import render
import datetime

def hello(request):
  return render(request, 'hello.html') 


def current_datetime(request):
  now = datetime.datetime.now()
  data = {'date': now}
  return render(request, 'current_date.html', data)

def time_plus(request, offset):
  try:
    hrs = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=hrs)
  data = {'date': dt, 'offset': hrs}
  return render(request, 'future_date.html', data)

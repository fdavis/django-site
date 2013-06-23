from django.shortcuts import render
import datetime

def hello(request):
  return render(request, 'hello.html') 

def show_meta(request):
  values = request.META.items()
  values.sort()
  html = []
  for k, v in values:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return render(request, 'message.html', {'message': html}) 

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

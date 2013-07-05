from django.shortcuts import render
import datetime

def hello(request):
  return render(request, 'hello.html') 

def show_meta(request):
  values = request.META.items()
  values.append('request.path', request.path)
  values.append('request.get_host', request.get_host())
  values.append('request.get_full_path', request.get_full_path())
  values.append('request.is_secure', request.is_secure())
  values.sort()
  #html = []
  #for k, v in values:
  #  html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return render(request, 'message.html-dict', {'message': values})

def current_datetime(request):
  now = datetime.datetime.now()
  data = {'date': now}
  return render(request, 'current_date.html', data)

def time_plus(request, hours):
  try:
    hrs = int(hours)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=hrs)
  data = {'date': dt, 'offset': hrs}
  return render(request, 'future_date.html', data)

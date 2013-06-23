from django.shortcuts import render
import datetime

def hello(request):
  return render(request, 'hello.html') 

def show_meta(request):
  values = request.META
  values["request.path"] = request.path
  values["request.get_host"] = request.get_host()
  values['request.get_full_path'] = request.get_full_path()
  values['request.is_secure'] = request.is_secure()
  #html = []
  #for k, v in values:
  #  html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return render(request, 'message.html', {'message': values})

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

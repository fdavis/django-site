from django.shortcuts import render

def search_form(request, callback={}):
  return render(request, 'search_form.html', callback)

def search(request):
  if request.GET.get('q', None):
    message = 'Your searched for: %r' % request.GET['q']
    return render(request, 'message.html', {'message': message})

  callback = {'message':  'You submitted an empty form.', 'error': True}
  return search_form(request, callback)

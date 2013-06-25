from django.shortcuts import render

def search_form(request, callback={}):
  return render(request, 'search_form.html', callback)

def search(request):
  error = False
  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      error = True
    else:
      message = 'Your searched for: %r' % q
      return render(request, 'message.html', {'message': message})
  
  callback = {'message':  'You submitted an empty form.', 'error': True}
  return search_form(request, callback)

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
    ip = x_forwarded_for.split(',')[0]
  else:
    ip = request.META.get('REMOTE_ADDR')
  httpMsg = "You are at ./index.html"
  httpMsg += "<br>Your client IP is {}".format(ip)
  httpMsg += "<br><br>"
  #for i in request.META.keys():
  #  if
  list_fields = [
     'REQUEST_METHOD','REQUEST_URI','SERVER_PROTOCOL','HTTP_HOST',
     'SERVER_NAME','SERVER_ADDR','SERVER_PORT',
     'REMOTE_ADDR','REMOTE_PORT','HTTP_USER_AGENT','HTTP_COOKIE']
  for i in list_fields:
    httpMsg += "<br>{} = {}".format(i, request.META.get(i))
  return HttpResponse(httpMsg)

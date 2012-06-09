from django.template import Context, loader
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request, template='index.html'):
	c = default_context()
	return render_to_response(template, c)
	
def wedding(request, template='wedding.html'):
	c = default_context()
	return render_to_response(template, c)
	
def gallery(request, template='gallery.html'):
	c = default_context()
	return render_to_response(template, c)

def contact(request, template='contact.html'):
	c = default_context()
	return render_to_response(template, c)
	
def default_context():
	return Context({"CSS_CDN": settings.CSS_CDN, "IMAGES_CDN": settings.IMAGES_CDN, "JS_CDN": settings.JS_CDN})
from django.shortcuts import render
from functions import *

def home(request): 
	title = "Website"
	investReturn = roi(102)
	states = ["California", "Arizona", "Texas", "New York", "Washington DC"]
	agents = {"California": ["Tom Delaney", "Nick Gate", "Jim Morse"]}

	return render(request, 'home.html', {'title': title, 'roi': investReturn, 'states': states, 'agents': agents })

def about(request):
	title = "Welcome to the About Page"
	aboutText = "My about page"

	return render(request, 'about.html', {'title':title, 'about':aboutText})
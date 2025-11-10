from django.shortcuts import render


def home(request):
	"""Render the main homepage template."""
	return render(request, 'home.html')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def chapters(request):
    return render(request, 'chapters.html')

def committees(request):
    return render(request, 'committees.html')

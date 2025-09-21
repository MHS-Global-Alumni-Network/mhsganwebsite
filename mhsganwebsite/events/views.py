from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event

# Create your views here.
@login_required()
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events')
    else:
        event_form = EventForm()
    return render(request, 'events/create_event.html', {'form': event_form})


def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})

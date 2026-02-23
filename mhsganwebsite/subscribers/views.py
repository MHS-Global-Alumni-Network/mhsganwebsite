from django.shortcuts import render, redirect
from .forms import SubscriberForm

def create_subscriber(request):
    if request.method == 'POST':
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            return redirect('confirm_subscription')
    else:
        subscriber_form = SubscriberForm()
    return render(request, 'subscribers/create_subscriber.html', {'form': subscriber_form})

def confirm_subscription(request):
    return render(request, 'subscribers/subscriber_confirmation.html')

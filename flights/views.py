from django.shortcuts import get_object_or_404, render

from .models import Flight


def index(request):
    return render(
        request,
        "flights/index.html",
        {"flights": Flight.objects.all()},
    )


def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(
        request,
        "flights/flight.html",
        {"flight": flight},
    )


from django.test import TestCase
from django.urls import reverse

from .models import Airport, Flight


class FlightTests(TestCase):
    def setUp(self) -> None:
        self.a1 = Airport.objects.create(code="AAA", city="CityA")
        self.a2 = Airport.objects.create(code="BBB", city="CityB")
        self.flight = Flight.objects.create(
            origin=self.a1, destination=self.a2, duration=100
        )

    def test_str_methods(self) -> None:
        self.assertEqual(str(self.a1), "CityA (AAA)")
        self.assertIn("AAA to BBB", str(self.flight))

    def test_index_view_lists_flights(self) -> None:
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AAA")
        self.assertContains(response, "BBB")

    def test_flight_view_shows_details(self) -> None:
        response = self.client.get(reverse("flight", args=[self.flight.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CityA")
        self.assertContains(response, "CityB")


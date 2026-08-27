from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Rezervim

class KontaktViewTests(TestCase):
	def test_valid_contact_form_saves_reservation(self):
		response = self.client.post(
			reverse("kontakt"),
			{
				"emri": "Arben Rama",
				"telefoni": "+355 69 123 4567",
				"email": "arben@example.com",
				"sherbimi": "kontroll",
				"data": (date.today() + timedelta(days=1)).isoformat(),
				"ora": "mengjes",
				"mesazhi": "Kontroll rutinë",
			},
		)

		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context["success"])
		self.assertEqual(Rezervim.objects.count(), 1)

	def test_invalid_contact_form_does_not_save(self):
		response = self.client.post(reverse("kontakt"), {"emri": "A"})

		self.assertEqual(response.status_code, 200)
		self.assertIn("emri", response.context["errors"])
		self.assertEqual(Rezervim.objects.count(), 0)

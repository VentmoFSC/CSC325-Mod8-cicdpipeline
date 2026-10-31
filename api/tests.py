from django.test import TestCase
from django.urls import reverse


class HelloApiTests(TestCase):
    def test_get_returns_success_message(self):
        response = self.client.get(reverse("hello_api"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "message": "Hello from CSC 325!",
                "status": "success",
            },
        )

    def test_post_is_not_allowed(self):
        response = self.client.post(reverse("hello_api"))

        self.assertEqual(response.status_code, 405)

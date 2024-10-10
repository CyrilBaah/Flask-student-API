from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTestCase(TestCase):
    """Test suite for the HealthCheck API view."""

    def setUp(self):
        # Set up the API client
        self.client = APIClient()

    def test_health_check(self):
        """Test the Health Check endpoint for success response"""
        response = self.client.get(
            "/healthcheck/"
        )  # Adjust the URL to match the route in your app

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the content of the response
        expected_response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "Backend launched successfully",
            "version": "0.1.0",
        }
        self.assertEqual(response.json(), expected_response)

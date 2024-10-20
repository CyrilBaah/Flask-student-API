from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Student


class StudentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student1 = Student.objects.create(name="John Doe", age=16, grade="10th")
        self.student2 = Student.objects.create(name="Jane Doe", age=17, grade="11th")
        self.list_url = reverse(
            "student-list"
        )  # This should match the URL for StudentList view
        self.detail_url = reverse(
            "student-detail", kwargs={"pk": self.student1.pk}
        )  # For individual student

    def test_get_student_list(self):
        """Test that we can get the list of students"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "John Doe")

    def test_create_student(self):
        """Test that we can create a new student"""
        data = {"name": "New Student", "age": 15, "grade": "9th"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Student")
        self.assertEqual(Student.objects.count(), 3)

    def test_get_student_detail(self):
        """Test retrieving a student by their ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Doe")

    def test_update_student(self):
        """Test updating a student's details"""
        data = {"name": "John Smith", "age": 16, "grade": "10th"}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.name, "John Smith")

    def test_delete_student(self):
        """Test deleting a student by their ID"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 1)

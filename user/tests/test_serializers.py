from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from user.serializers import UserSerializer, AuthTokenSerializer

User = get_user_model()

class UserSerializerTest(TestCase):

    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        self.serializer = UserSerializer(data=self.user_data)

    def test_user_serializer_valid(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data["username"], "testuser")

    def test_user_serializer_create(self):
        self.serializer.is_valid()
        user = self.serializer.save()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword"))

    def test_user_serializer_update(self):
        user = User.objects.create_user(**self.user_data)
        new_data = {"username": "updateduser", "password": "newpassword"}
        serializer = UserSerializer(instance=user, data=new_data, partial=True)

        # Перевіряємо, що сериалізатор дійсний
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.username, "updateduser")
        self.assertTrue(updated_user.check_password("newpassword"))


class AuthTokenSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        self.valid_credentials = {
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        self.invalid_credentials = {
            "email": "wrong@example.com",
            "password": "wrongpassword"
        }
        self.serializer = AuthTokenSerializer(data=self.valid_credentials)

    def test_auth_token_serializer_valid(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data["user"], self.user)

    def test_auth_token_serializer_invalid_credentials(self):
        serializer = AuthTokenSerializer(data=self.invalid_credentials)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_auth_token_serializer_authenticate_user(self):
        self.serializer.is_valid()
        self.assertIn("user", self.serializer.validated_data)
        self.assertEqual(self.serializer.validated_data["user"], self.user)

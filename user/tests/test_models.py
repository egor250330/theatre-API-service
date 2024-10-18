from django.test import TestCase
from user.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="newuser",
            password="newpassword",
            email="newuser@example.com"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "newuser")
        self.assertEqual(self.user.email, "newuser@example.com")
        self.assertTrue(self.user.check_password("newpassword"))

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_user_default_values(self):
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, False)

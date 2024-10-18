from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from theatre.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    User,
    Reservation,
    Ticket,
    Performance
)


class ActorModelTest(TestCase):
    def test_actor_creation_without_image(self):
        actor = Actor.objects.create(first_name="Test", last_name="Actor")
        self.assertEqual(actor.first_name, "Test")
        self.assertEqual(actor.last_name, "Actor")

    def test_actor_creation_with_image(self):
        image_file = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        actor = Actor.objects.create(
            first_name="Test",
            last_name="Actor",
            image=image_file
        )
        self.assertEqual(actor.first_name, "Test")
        self.assertEqual(actor.last_name, "Actor")
        self.assertIsNotNone(actor.image)
        self.assertTrue(actor.image.name.startswith("upload/images/actors/"))


class GenreModelTest(TestCase):
    def test_genre_creation(self):
        genre = Genre.objects.create(name="Drama")
        self.assertEqual(genre.name, "Drama")
        self.assertEqual(Genre.objects.count(), 1)

    def test_genre_name_max_length(self):
        genre = Genre.objects.create(name="Comedy")
        max_length = genre._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class PlayModelTest(TestCase):
    def test_play_creation(self):
        play = Play.objects.create(title="Hamlet")
        self.assertEqual(play.title, "Hamlet")
        self.assertEqual(Play.objects.count(), 1)

    def test_play_title_max_length(self):
        play = Play.objects.create(title="Hamlet")
        max_length = play._meta.get_field("title").max_length
        self.assertEqual(max_length, 50)

    def test_play_creation_with_description(self):
        play = Play.objects.create(
            title="Hamlet",
            description="A tragedy by Shakespeare."
        )
        self.assertEqual(
            play.description,
            "A tragedy by Shakespeare."
        )


class TheatreHallModelTest(TestCase):
    def test_theatre_hall_creation(self):
        hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20,
            image=None
        )
        self.assertEqual(hall.name, "Main Hall")
        self.assertEqual(hall.rows, 10)
        self.assertEqual(hall.seats_in_row, 20)
        self.assertFalse(hall.image)
        self.assertEqual(TheatreHall.objects.count(), 1)

    def test_theatre_hall_name_max_length(self):
        hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )
        max_length = hall._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_theatre_hall_rows_and_seats(self):
        hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=5, seats_in_row=15
        )
        self.assertGreaterEqual(hall.rows, 1)
        self.assertGreaterEqual(hall.seats_in_row, 1)

    def test_theatre_hall_image_field(self):
        hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20,
            image=None
        )
        self.assertFalse(hall.image)


class PerformanceModelTest(TestCase):
    def setUp(self):
        self.play = Play.objects.create(title="Hamlet")
        self.hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.hall,
            show_time=timezone.now()
        )

    def test_performance_creation(self):
        self.assertEqual(self.performance.play, self.play)
        self.assertEqual(self.performance.theatre_hall, self.hall)
        self.assertIsInstance(self.performance.show_time, timezone.datetime)


class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.reservation = Reservation.objects.create(user=self.user)

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.user, self.user)
        self.assertIsInstance(self.reservation.created_at, timezone.datetime)


class TicketModelTest(TestCase):
    def setUp(self):
        self.play = Play.objects.create(title="Hamlet")
        self.hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.hall,
            show_time=timezone.now()
        )
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket = Ticket.objects.create(
            row=1,
            seat=1,
            performance=self.performance,
            reservation=self.reservation
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.row, 1)
        self.assertEqual(self.ticket.seat, 1)
        self.assertEqual(self.ticket.performance, self.performance)
        self.assertEqual(self.ticket.reservation, self.reservation)

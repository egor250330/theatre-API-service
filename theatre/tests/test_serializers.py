from rest_framework import serializers
from rest_framework.test import APITestCase
from theatre.models import Actor, Genre, Play, TheatreHall, Reservation, User, Ticket, Performance
from theatre.serializers import ActorSerializer, ActorImageSerializer, GenreSerializer, PlaySerializer, \
    TheatreHallSerializer, TheatreHallImageSerializer, ReservationSerializer, PerformanceSerializer, TicketSerializer


class ActorSerializersTest(APITestCase):
    def setUp(self):
        self.actor = Actor.objects.create(
            first_name="Tom",
            last_name="Hanks",
            image="image_url.jpg"
        )

    def test_actor_serializer_fields(self):
        serializer = ActorSerializer(instance=self.actor)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "first_name", "last_name", "image"})
        self.assertEqual(data["first_name"], self.actor.first_name)
        self.assertEqual(data["last_name"], self.actor.last_name)
        self.assertEqual(data["image"], self.actor.image.url)

    def test_actor_image_serializer_fields(self):
        serializer = ActorImageSerializer(instance=self.actor)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "image"})
        self.assertEqual(data["image"], self.actor.image.url)


class GenreSerializerTest(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            name="Drama"
        )

    def test_genre_serializer_fields(self):
        serializer = GenreSerializer(instance=self.genre)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "name"})
        self.assertEqual(data["name"], self.genre.name)


class PlaySerializerTest(APITestCase):
    def setUp(self):
        self.play = Play.objects.create(
            title="Hamlet",
            description="The story about Hamlet"
        )

    def test_play_serializer_fields(self):
        serializer = PlaySerializer(instance=self.play)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "title", "description"})
        self.assertEqual(data["title"], self.play.title)
        self.assertEqual(data["description"], self.play.description)


class TheatreHallSerializerTest(APITestCase):
    def setUp(self):
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall",
            rows=10,
            seats_in_row=20,
            image="image_url.jpg"
        )

    def test_theatre_hall_serializer_fields(self):
        serializer = TheatreHallSerializer(instance=self.theatre_hall)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "name", "rows", "seats_in_row", "image"})
        self.assertEqual(data["name"], self.theatre_hall.name)
        self.assertEqual(data["rows"], self.theatre_hall.rows)
        self.assertEqual(data["seats_in_row"], self.theatre_hall.seats_in_row)
        self.assertEqual(data["image"], self.theatre_hall.image.url)

    def test_theatre_hall_image_serializer_fields(self):
        serializer = TheatreHallImageSerializer(instance=self.theatre_hall)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "image"})
        self.assertEqual(data["image"], self.theatre_hall.image.url)


class ReservationSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.reservation = Reservation.objects.create(
            user=self.user,
            created_at="2024-10-17T10:00:00Z"
        )

    def test_reservation_serializer_fields(self):
        serializer = ReservationSerializer(instance=self.reservation)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "created_at", "user"})
        self.assertEqual(data["user"], self.user.id)
        self.assertEqual(data["created_at"], self.reservation.created_at.isoformat().replace("+00:00", "Z"))


class PerformanceAndTicketSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.play = Play.objects.create(title="Hamlet", description="A tragedy by Shakespeare")
        self.theatre_hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=20)
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2024-10-17T19:00:00Z"
        )
        self.reservation = Reservation.objects.create(user=self.user, created_at="2024-10-17T10:00:00Z")
        self.ticket = Ticket.objects.create(
            row=1,
            seat=5,
            performance=self.performance,
            reservation=self.reservation
        )

    def test_performance_serializer_fields(self):
        serializer = PerformanceSerializer(instance=self.performance)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "play", "theatre_hall", "show_time"})
        self.assertEqual(data["play"]["id"], self.play.id)
        self.assertEqual(data["play"]["title"], self.play.title)
        self.assertEqual(data["theatre_hall"]["id"], self.theatre_hall.id)
        self.assertEqual(data["theatre_hall"]["name"], self.theatre_hall.name)
        self.assertEqual(data["show_time"], self.performance.show_time)

    def test_ticket_serializer_fields(self):
        serializer = TicketSerializer(instance=self.ticket)
        data = serializer.data

        self.assertEqual(set(data.keys()), {"id", "row", "seat", "performance", "reservation"})
        self.assertEqual(data["row"], self.ticket.row)
        self.assertEqual(data["seat"], self.ticket.seat)
        self.assertEqual(data["performance"]["id"], self.performance.id)
        self.assertEqual(data["reservation"]["id"], self.reservation.id)

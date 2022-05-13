from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

# Create your models here.
class User(AbstractUser):
    location = models.CharField(max_length=64, default="Antwerp")
    display_name = models.CharField(max_length=32, default="John Doe")


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        # order alphabetically
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    @property
    def count_active_requests(self):
        return Request.objects.filter(
            category=Category.objects.get(name=self.name),
            ended_manually=False,
        ).count()

    @property
    def count_active_donations(self):
        return Donation.objects.filter(
            category=Category.objects.get(name=self.name),
            ended_manually=False,
        ).count()

    def __str__(self) -> str:
        return str(self.name)


class Request(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="requests",
    )

    creator: User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requests"
    )

    date_created = models.DateTimeField(auto_created=True, default=timezone.now)

    ended_manually = models.BooleanField(default=False)

    def __str__(self):
        return f"Request #{self.id}: {self.creator.username}"

    def ended(self):
        return self.ended_manually

    def get_type(self):
        return "request"

    def get_verb(self):
        return "donate"


class Donation(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="donations",
    )

    creator: User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="donations"
    )

    date_created = models.DateTimeField(auto_created=True, default=timezone.now)

    ended_manually = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation #{self.id}: {self.creator.username}"

    def ended(self):
        return self.ended_manually

    def get_type(self):
        return "donation"

    def get_verb(self):
        return "get"

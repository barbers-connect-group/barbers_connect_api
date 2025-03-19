import os

from django.db import models
from django.contrib.auth.models import User


def upload_review(instance, filename):
    name, extension = os.path.splitext(filename)
    return '/'.join([f'reviews/image_{instance.pk}{extension}'])


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    barbershop = models.ForeignKey('BarberShop', on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(6)])
    image_path = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=upload_review, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='created_reviews', null=True)
    updated_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='updated_reviews', null=True)

    def __str__(self):
        return f"{self.user.username} - {self.barbershop.name} ({self.rating}/5)"

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        if self.image and 'temp_' in self.image.name:
            self.image.name = f"reviews/image_{self.id}"
        super().save(*args, **kwargs)

        if self.image and self.image.url:
            self.image_path = self.image.url
            super().save()

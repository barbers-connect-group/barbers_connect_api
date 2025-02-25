from django.db import models

from api.models import Tag


class BarberShop(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    start_shift = models.TimeField(null=True)
    end_shift = models.TimeField(null=True)
    tags = models.ManyToManyField(Tag, related_name="barbearias")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='created_barbershops', null=True)
    updated_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='updated_barbershops', null=True)

    def __str__(self):
        return self.name

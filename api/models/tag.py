from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='created_tags', null=True)
    updated_by = models.ForeignKey(to='auth.User', on_delete=models.PROTECT, related_name='updated_tags', null=True)


    def __str__(self):
        return self.name

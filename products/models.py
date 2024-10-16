from django.db import models


class Product(models.Model):
    article     = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=10000, blank=True)
    vendor_code = models.TextField(max_length=1000, blank=True)
    imt_name    = models.TextField(max_length=1000, blank=True)
    contents    = models.TextField(max_length=1000, blank=True)
    slug        = models.TextField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article

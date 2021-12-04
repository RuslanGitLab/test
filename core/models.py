from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# # Create your models here.
class Buyer(AbstractUser):
    ...


class PriceMixin(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class Pan(PriceMixin):
    vendor_choices = [("tefal", "Tefal")]
    vendor = models.CharField(max_length=128, choices=vendor_choices)
    diameter = models.PositiveIntegerField()
    purchases = GenericRelation("Purchase", related_name="gfc_purchases")

    def __str__(self):
        return f"Сковорода фирмы: {self.vendor}"


class Potato(PriceMixin):
    country_choices = [("bel", "Буларусь")]
    id = models.UUIDField(primary_key=True)
    country = models.CharField(max_length=128)
    purchases = GenericRelation("Purchase", related_name="gfc_purchases")

    def __str__(self):
        return f"Картошка из страны: {self.country}"


class Purchase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.CharField(max_length=128)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="purchases")

    product = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"purchase_id: {self.id}, CT: {self.content_type}, object_id: {self.object_id}"


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


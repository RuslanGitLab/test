from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Создадим модель нашего покупателя, просто унаследовав пользователя Django
class Buyer(AbstractUser):
    ...


class PriceMixin(models.Model):
    """
        Абстрактная родительская таблица для общих полей и методов, чтобы не повторяться
    """
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class Pan(PriceMixin):
    """
        Модель описывающая таблицу с товаром типа: Сковорода
    """
    VENDOR_TEFAL = "tefal", "Tefal"

    vendor_choices = [(VENDOR_TEFAL[0], VENDOR_TEFAL[1])]
    vendor = models.CharField(max_length=128, choices=vendor_choices)
    diameter = models.PositiveIntegerField()

    purchases = GenericRelation("Purchase", related_query_name="pan", related_name="pans")

    def __str__(self):
        return f"Сковорода фирмы: {self.get_vendor_display()}, {self.diameter} sm"


class Potato(PriceMixin):
    """
        Модель описывающая таблицу с товаром типа: Картофель
    """

    COUNTRY_BEL = "bel", "Беларусь"
    country_choices = [(COUNTRY_BEL[0], COUNTRY_BEL[1]), ]

    id = models.UUIDField(primary_key=True)
    country = models.CharField(max_length=128, choices=country_choices)

    purchases = GenericRelation("Purchase", related_query_name="potato", related_name="potatoes")

    def __str__(self):
        return f"Картофель из страны: {self.get_country_display()}"


class Purchase(models.Model):
    """
        Объект описывающий сущность покуаки чего либо.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField()
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="purchases")

    # Согласно документации, создаём поля для хранения ContentType и object_id
    # https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.CharField(max_length=128)

    # Создаём генерируемый внешний ключ, который может быть связан с продуктами разных типов: сковорода, картошка и тд
    product = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        # кстати тут у нас явный пример полиморфизма, у всех продуктов будет вызван метод __str__, но вернётся разный
        # результат для каждого продукта
        return f"purchase_id: {self.id}, product: {self.product}"


class Order(models.Model):
    """
        Модель описывающая заказ, содержит связь с покупками, через related_name="purchases", см core/models.py:52
    """
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

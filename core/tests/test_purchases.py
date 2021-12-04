import uuid

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from core.models import Pan, Buyer, Purchase, Potato, Order


# python manage.py test core.tests.test_purchases
class PurchasesTest(TestCase):
    POTATO_UUID = "b5a32d62-5535-11ec-a799-049226578ae5"

    def test_order_creation(self):
        buyer = Buyer.objects.create(id=1, username="Alex")
        pan = Pan.objects.create(id=1, vendor='tefal', diameter=30, price=1500)
        potato = Potato.objects.create(id=self.POTATO_UUID, country="bel", price=45.5)
        order = Order.objects.create(buyer=buyer)

        ct_pan, ct_potato = ContentType.objects.get_for_model(Pan), ContentType.objects.get_for_model(Potato)

        Purchase.objects.create(
            count=3, content_type=ct_potato, object_id=potato.id, order=order
        )
        Purchase.objects.create(count=1, content_type=ct_pan, object_id=pan.id, order=order)

        print(order.purchases.all())
        self.assertEqual(order.purchases.count(), 2)

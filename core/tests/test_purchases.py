import uuid

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from core.models import Pan, Buyer, Purchase, Potato, Order


# python manage.py test core.tests.test_purchases
class PurchasesTest(TestCase):
    POTATO_UUID = "b5a32d62-5535-11ec-a799-049226578ae5"

    def test_order_creation(self):
        # Создаём покупателя, сковороду и белорусскую картошку :)
        buyer = Buyer.objects.create(id=1, username="Alex")
        pan = Pan.objects.create(id=1, vendor=Pan.VENDOR_TEFAL[0], diameter=30, price=1500)
        potato = Potato.objects.create(id=self.POTATO_UUID, country=Potato.COUNTRY_BEL[0], price=45.5)

        # Создаем заказ
        order = Order.objects.create(buyer=buyer)

        # получим ContentType для сковороды и картошки
        ct_pan, ct_potato = ContentType.objects.get_for_model(Pan), ContentType.objects.get_for_model(Potato)

        # Создадим две покупки, 3 кг картошки, 1 сковороды
        Purchase.objects.create(count=3, content_type=ct_potato, object_id=potato.id, order=order)
        Purchase.objects.create(count=1, content_type=ct_pan, object_id=pan.id, order=order)

        # Првоерим что покупки привязались к заказу
        self.assertEqual(order.purchases.count(), 2)

        # Теперь мы можем вывести все покупки товара картофель или сковрода
        print(pan.purchases.all())
        print(potato.purchases.all())

        # Аналогично все покупки нашего заказа
        print(order.purchases.all())

        # Или даже все сковороды в заказе от заданного производителя
        print(order.purchases.filter(pan__vendor="tefal"))
        # <QuerySet [<Purchase: purchase_id: 1, CT: core | potato, object_id: b5a32d62-5535-11ec-a799-049226578ae5>,
        #            <Purchase: purchase_id: 2, CT: core | pan, object_id: 1>]>

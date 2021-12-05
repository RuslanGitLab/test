
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from core.models import Pan, Buyer, Purchase, Potato, Order


# python manage.py test core.tests.test_purchases
class PurchasesTest(TestCase):
    POTATO_UUID = "b5a32d62-5535-11ec-a799-049226578ae5"
    POTATO_UUID2 = "b5a32d62-5535-11ec-a799-049226578ae6"

    def test_order_creation(self):
        # Создаём покупателей, сковороду и белорусскую картошку :)
        buyer_alex = Buyer.objects.create(id=1, username="Alex")
        buyer_boris = Buyer.objects.create(id=2, username="Boris")

        pan_tefal = Pan.objects.create(id=1, vendor=Pan.VENDOR_TEFAL[0], diameter=30, price=1500)
        pan_fissman = Pan.objects.create(id=2, vendor=Pan.VENDOR_FISSMAN[0], diameter=35, price=1700)
        potato_bel = Potato.objects.create(id=self.POTATO_UUID, country=Potato.COUNTRY_BEL[0], price=45.5)
        potato_rus = Potato.objects.create(id=self.POTATO_UUID2, country=Potato.COUNTRY_RUS[0], price=35.5)

        # Создаем заказы
        order_alex = Order.objects.create(buyer=buyer_alex)
        order_boris = Order.objects.create(buyer=buyer_boris)

        # получим ContentType для сковороды и картошки
        ct_pan, ct_potato = ContentType.objects.get_for_model(Pan), ContentType.objects.get_for_model(Potato)

        # Создадим две покупки, 3 кг картошки, 1 сковороды
        Purchase.objects.create(count=2.75, content_type=ct_potato, object_id=potato_rus.id, order=order_alex)
        Purchase.objects.create(count=3.5, content_type=ct_potato, object_id=potato_bel.id, order=order_alex)
        Purchase.objects.create(count=1, content_type=ct_pan, object_id=pan_tefal.id, order=order_alex)

        Purchase.objects.create(count=4.5, content_type=ct_potato, object_id=potato_bel.id, order=order_boris)
        Purchase.objects.create(count=1, content_type=ct_pan, object_id=pan_fissman.id, order=order_boris)

        # Првоерим что покупки привязались к заказу
        self.assertEqual(order_boris.purchases.count(), 2)
        self.assertEqual(order_alex.purchases.count(), 3)

        # Теперь мы можем вывести все покупки товара картофель или сковрода
        print(potato_rus.purchases.all())
        print(potato_bel.purchases.all())

        # Все заказы покупателей
        print(buyer_alex.orders.all())
        print(buyer_boris.orders.all())

        # Все покупки заказа
        print(order_boris.purchases.all())
        print(order_alex.purchases.all())

        # Или даже все сковороды в заказе от заданного производителя
        print(order_alex.purchases.filter(pan__vendor=Pan.VENDOR_TEFAL[0]))
        # Или весь беларусский картофель в заказе
        print(order_alex.purchases.filter(potato__country=Potato.COUNTRY_BEL[0]))

        # наглядно можно увидеть, что продукты действительно разного типа
        for p in order_alex.purchases.all():
            print(p.product)

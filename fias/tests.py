import logging

from django.test import TestCase
from fias.models import FIASNode
# Create your tests here.
logger = logging.getLogger()
logger.level = logging.INFO


class TestMPTT(TestCase):

    def test_hierarchy(self):
        country = FIASNode.objects.create(name="Россия", type=FIASNode.COUNTRY)
        country_dis = FIASNode.objects.create(name="ЦФО", type=FIASNode.FEDERAL_DISTRICT_TYPE, parent=country)
        city = FIASNode.objects.create(name="Воронеж", type=FIASNode.CITY_TYPE, parent=country_dis)
        city_dis = FIASNode.objects.create(name="Железнодорожный рн", type=FIASNode.CITY_DISTRICT_TYPE, parent=city)
        street = FIASNode.objects.create(name="Северная", type=FIASNode.STREET_TYPE, parent=city_dis)
        house = FIASNode.objects.create(name="11", type=FIASNode.HOUSE_TYPE, parent=street)

        logger.info("Country descendants")
        logger.info(country.get_descendants())

        assert country.get_descendants()

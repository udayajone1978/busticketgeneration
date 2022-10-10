from django.test import TestCase
from onlinebus.models import bus


class bustestcase(TestCase):
    def setUp(self):
        print("Setup Activity")
        bus.objects.create(bus_name="Ganga",bus_no=21,start="Thanjavur",end="Chennai",seats=150,balanseat=4,amount=450,date="2022-7-10",time="04:52")
        bus.objects.create(bus_name="Ranga",bus_no=25,start="Thanjavur",end="Chennai",seats = 150, balanseat = 4, amount = 450, date="2022-7-10", time="04:55")

    def test_bus_info(self):
        print("Testing Bus Information")
        qs=bus.objects.all()
        self.assertEqual(qs.count(),2)
        b1=bus.objects.get(bus_name="Ganga")
        b2=bus.objects.get(bus_name="Ranga")
        self.assertEqual(b1.get_start() ,"Thanjavur")
        self.assertEqual(b2.get_end(),"Chennai")
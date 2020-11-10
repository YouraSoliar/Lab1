import unittest
from app import main, my_good_fun, AmPm


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
        # Ваш захист
        self.assertTrue(True)

    def test_my_fun(self):
        self.assertEqual(my_good_fun(), "success")

    def AmPm(self):
        self.assertEqual(get_time_of_day_name("01:00:00 AM"), "day")
        self.assertEqual(get_time_of_day_name("01:00:00 PM"), "night")

        try:
            get_time_of_day_name("some text")
            self.assertTrue(False)
        except RuntimeError:
            self.assertTrue(True)
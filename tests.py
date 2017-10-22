import unittest
from invoice import Invoice
from main import ENDPOINT, payload


class TestInvoiceMethods(unittest.TestCase):
    """
    Test para los métodos de la clase Invoice
    """
    # Endpoint a la api
    endpoint = ENDPOINT
    # Payload para el endpoint
    payload = payload
    # Clase Invoice
    klass = None

    def __init__(self, *args, **kwargs):
        super(TestInvoiceMethods, self).__init__(*args, **kwargs)
        """
        Constructor
        """
        self.klass = Invoice(self.endpoint, self.payload)

    def test_make_request(self):
        """
        Testeo si _make_request retorna como status 200
        """
        self.payload['start'] = "2017-01-01"
        self.payload['finish'] = "2017-01-31"
        self.assertEqual(self.klass._make_request().status_code, 200)

    def test_get_total_days_month(self):
        """
        Testeo el último día del mes de enero
        """
        self.assertEqual(self.klass._get_total_days_month(1), 31)

    def test_get_total_weeks_month(self):
        """
        Testeo la cantidad de semanas del mes de enero
        """
        self.assertEqual(self.klass._get_total_weeks_month(1), 5)

    def test_get_total_invoices(self):
        """
        Testeo la cantidad de facturas retornadas
        """
        self.assertTrue(self.klass.get_total_invoices())

if __name__ == '__main__':
    unittest.main()

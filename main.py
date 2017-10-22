from invoice import Invoice

# Constantes
ENDPOINT = 'http://34.209.24.195/facturas'
ID = 'a61513e3-add2-412a-a26e-5993087b8888'

# Parámetros para el endpoint
payload = {
    'id': ID,
    'start': '',
    'finish': ''
}

if __name__ == "__main__":
    # Obtengo el total de facturas anuales
    invoice = Invoice(ENDPOINT, payload)
    params = invoice.get_total_invoices()

    # Informo los resultados
    print("El total de facturas son: " + params['total_invoices'])
    print("Total de peticiones realizadas: " + params['total_request'])

import streamlit as st

# Función para leer las credenciales desde el archivo
def leer_credenciales(archivo):
    credenciales = {}
    with open(archivo, 'r') as f:
        for linea in f:
            nombre, valor = linea.strip().split('=')
            credenciales[nombre] = valor
    return credenciales

# Leer las credenciales de PayPal
credenciales = leer_credenciales('paypal_credentials.txt')
client_id = credenciales['client_id']
secret = credenciales['secret']
email = credenciales['email']

# Función para calcular el total
def calcular_total(cantidad, precio):
    return cantidad * precio

# Título del formulario
st.title("Formulario de Pagos")

# Entrada de datos
producto = st.text_input("Producto")
cantidad = st.number_input("Cantidad", min_value=1, step=1)
precio = st.number_input("Precio", min_value=0.0, step=0.01)

# Calcular el total
total = calcular_total(cantidad, precio)
st.write(f"Total: ${total:.2f}")

# Botón de PayPal
st.markdown(f"""
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_xclick">
<input type="hidden" name="business" value="{email}">
<input type="hidden" name="item_name" value="{producto}">
<input type="hidden" name="amount" value="{total:.2f}">
<input type="hidden" name="currency_code" value="USD">
<input type="hidden" name="client_id" value="{client_id}">
<input type="hidden" name="secret" value="{secret}">
<input type="submit" value="Pagar con PayPal">
</form>
""", unsafe_allow_html=True)

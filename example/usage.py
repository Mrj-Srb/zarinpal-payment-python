from zarinpal_payment import ZarinPal

# Create an instance of ZarinPal, use sandbox=True for using the sandbox environment
zarinpal = ZarinPal(merchant_id="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", callback_url="Your callback URL", sandbox=True)

# Request a payment
response = zarinpal.payment_request(amount=1000, description="Test payment")

# Get the authority from the response
authority = response.get("authority")

# Generate the payment URL
payment_url = zarinpal.generate_payment_url(authority)

# Verify the payment
verify_response = zarinpal.payment_verify(amount=1000, authority=authority)


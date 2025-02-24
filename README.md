### ZarinPal Python Payment Gateway Integration

This Python package provides a simple interface for integrating ZarinPal's payment gateway into your Python applications. It supports both sandbox and production environments, enabling you to test your payment functionality before going live.

---

### Features

- **Payment Request**: Send payment requests to ZarinPal's API.
- **Payment Verification**: Verify payment transactions to ensure success.
- **Generate Payment URL**: Generate a URL for users to complete their payment.
- **Sandbox & Production Modes**: Switch between sandbox for testing and the production environment for live payments.

---

### Installation

To install the package, run:

```bash
pip install zarinpal-payment
```

---

### Usage

Here is how to use the package to handle payment requests, verification, and generate payment URLs.

#### 1. Initialize ZarinPal Client

Create an instance of the `ZarinPal` class by passing your merchant ID, callback URL, and optionally, set the sandbox environment (`True` for testing, `False` for production):

```python
from zarinpal_payment.zarinpal import ZarinPal

zarinpal = ZarinPal(merchant_id="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", callback_url="Your callback URL", sandbox=True)
```

#### 2. Request a Payment

Use the `payment_request` method to initiate a payment request. Pass the amount and description (optional):

```python
response = zarinpal.payment_request(amount=1000, description="Test payment")
```

#### 3. Get the Authority

Extract the payment `authority` from the response to generate the payment URL:

```python
authority = response.get("data", {}).get("authority")
```

#### 4. Generate Payment URL

Use the `generate_payment_url` method to create a URL that will redirect users to the ZarinPal payment page:

```python
payment_url = zarinpal.generate_payment_url(authority)
```

#### 5. Verify the Payment

After the user completes the payment, verify the payment using the `payment_verify` method:

```python
verify_response = zarinpal.payment_verify(amount=1000, authority=authority)
```

---

### Example Code

```python
from zarinpal_payment.zarinpal import ZarinPal

# Create an instance of ZarinPal
# you can use any string but must be greater than 36 characters
zarinpal = ZarinPal(merchant_id="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", callback_url="Your callback URL", sandbox=True)

# Step 1: Request a payment
response = zarinpal.payment_request(amount=1000, description="Test payment")

# Step 2: Get the authority from the response
authority = response.get("data", {}).get("authority")

# Step 3: Generate the payment URL
payment_url = zarinpal.generate_payment_url(authority)

# Step 4: Verify the payment
verify_response = zarinpal.payment_verify(amount=1000, authority=authority)

# Print the payment URL and verification response
print(payment_url)
print(verify_response)
```

---

### Configuration

- **merchant_id**: Your ZarinPal merchant ID.
- **callback_url**: The URL to which ZarinPal will redirect after the payment attempt.
- **sandbox**: Set this to `True` for testing in the sandbox environment or `False` for the live environment.

---

### Logging

The package uses Python's built-in `logging` module to log requests and responses. You can adjust the logging level to suit your needs.

---

### References

For more details about ZarinPal's API, please refer to the official documentation:

- [ZarinPal Payment API Documentation](https://next.zarinpal.com/paymentGateway/)
- [ZarinPal Payment Documentation](https://www.zarinpal.com/docs/paymentGateway/)

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


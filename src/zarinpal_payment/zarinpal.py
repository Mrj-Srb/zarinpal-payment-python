import requests
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ZarinPal:
    BASE_URLS = {
        "sandbox": "https://sandbox.zarinpal.com/pg/v4",
        "main": "https://payment.zarinpal.com/pg/v4"
    }

    def __init__(self, merchant_id: str, callback_url: str, sandbox: bool = False):
        self.merchant_id = merchant_id
        self.mode = "sandbox" if sandbox else "main"
        self.base_url = self.BASE_URLS[self.mode]

        self._payment_request_url = f"{self.base_url}/payment/request.json"
        self._payment_verify_url = f"{self.base_url}/payment/verify.json"
        self._payment_page_url = f"{self.base_url.replace('/v4', '')}/StartPay/"

        self._callback_url = callback_url

    def payment_request(self, amount: int, description: str = "پرداختی کاربر") -> dict:
        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "callback_url": self._callback_url,
            "description": description,
            "currency": "IRT"
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.post(self._payment_request_url, headers=headers, json=payload)
        json_response = response.json()
        if isinstance(json_response, dict):
            logging.info("Payment request Successful.")
            return json_response
        else:
            logging.error(f"Error in payment request: {json_response}")
            return json_response

    def payment_verify(self, amount: int, authority: str) -> dict:
        payload = {"merchant_id": self.merchant_id, "amount": amount, "authority": authority}
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.post(self._payment_verify_url, headers=headers, json=payload)
        json_response = response.json()
        if isinstance(json_response, dict):
            logging.info("Payment verify request Successful.")
            return json_response
        else:
            logging.error(f"Error in payment verify: {json_response}")
            return json_response

    def generate_payment_url(self, authority: str) -> str:
        return f"{self._payment_page_url}{authority}"









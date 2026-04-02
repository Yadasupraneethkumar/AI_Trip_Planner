import requests

class currencyconverter:
    def __init__(self,api_key:str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def convert(self, amount, from_currency: str, to_currency: str):
        """Convert the amount from one currency to another with strict type checking"""
        try:
            # --- DEBUG LOGGING (Check your terminal) ---
            print(f"DEBUG: amount={amount} (type: {type(amount)})")
            print(f"DEBUG: to_currency={to_currency} (type: {type(to_currency)})")

            # 1. Force Amount to Float
            if isinstance(amount, list):
                amount = amount[0]
            amount = float(amount)

            url = f"{self.base_url}/{from_currency}"
            response = requests.get(url, timeout=5)
        
            if response.status_code != 200:
                return f"API Error: {response.status_code}"

            data = response.json()
            rates = data.get("conversion_rates", {})
        
            # 2. Extract and Force Rate to Float
            raw_rate = rates.get(to_currency)
            if raw_rate is None:
                return f"Error: Currency {to_currency} not found."
        
            print(f"DEBUG: raw_rate={raw_rate} (type: {type(raw_rate)})")

            if isinstance(raw_rate, list):
                raw_rate = raw_rate[0]
        
            final_rate = float(raw_rate)

            # 3. Final Calculation
            return amount * final_rate

        except Exception as e:
            # This will send the exact error back to your Streamlit frontend
            return f"Tool Error: {str(e)}"
import requests


class GenerativeAI:
    def __init__(self, history_file, gemini_api_key):
        self.api_key = gemini_api_key

        # The URL for the API request
        self.url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + self.api_key

        # Headers for the request
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.history = []

    def update_history(self, data_list):
        self.history = data_list

    def clear_history(self):
        self.history = [""]

    def generate_text(self, text: str):

        self.update_history(self.history + [{"role": "user", "parts": [{"text": text}]}])

        data = {
            "contents": self.history,
        }
        response = requests.post(self.url, json=data, headers=self.headers)

        result = response.json()['candidates'][0]['content']['parts'][0]['text']
        self.update_history(self.history + [{"role": "assistant", "parts": [{"text": result}]}])

        return result
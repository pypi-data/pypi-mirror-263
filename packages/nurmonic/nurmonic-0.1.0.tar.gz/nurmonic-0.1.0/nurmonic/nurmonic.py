# nurmonic.py

import os
import requests

class Nurmonic:
    def __init__(self, api_key=None):
        self.api_key = api_key if api_key is not None else os.environ.get('NURMONIC_KEY')
        self.base_url = 'https://nurmonic.xyz/chat/completions'

    def create_completion(self, messages, model):
        headers = {'Authorization': self.api_key}
        response = requests.post(self.base_url, json={'model': model, 'messages': messages}, headers=headers)
        response_data = response.json()
        if 'error' in response_data:
            if response_data['error'] == "Unknown model":
                raise Exception(f"Unknown model named {model}")
            else:
                raise Exception(response_data['error'])
        return response_data
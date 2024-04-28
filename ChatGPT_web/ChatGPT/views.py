from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests
import json

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        message = json.loads(request.body)['message']
        apiKey = ""
        url = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions'
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {apiKey}"
        }
        data = {
            "prompt": message,
            "max_tokens": 1000
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        chatbotResponse = 'No response'
        if response.status_code == 200:
            chatbotResponse = response.json()['choices'][0]['text']
        return JsonResponse({'chatbotResponse': chatbotResponse})


def index(request):
    return render(request,"ChatGPT/index.html")

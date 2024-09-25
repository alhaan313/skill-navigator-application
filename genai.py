import requests
from django.http import JsonResponse

# Add this function to trigger the Gemini API
def generate_practice_question():
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=YOUR_API_KEY'
    
    headers = {
        'Content-Type': 'application/json'
    }

    # Define the data payload (input for API)
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "Explain how AI works"}
                ]
            }
        ]
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Parse the response
        api_response = response.json()
        explanation = api_response.get('contents', [{}])[0].get('parts', [{}])[0].get('text', '')
        return explanation
    else:
        # Return error if API request fails
        return "Failed to generate question"

# Django view function where this is triggered based on some control flow
def practice_view(request):
    # Simulating some control flow
    user_score = 60  # Example control condition

    if user_score < 70:
        # If condition matches, trigger Gemini API for a practice question
        practice_question = generate_practice_question()
        return JsonResponse({'practice_question': practice_question})
    
    return JsonResponse({'message': 'No practice question needed'})

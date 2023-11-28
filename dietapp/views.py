from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def alice_webhook(request):
    # Only accept POST requests
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data['request']['original_utterance']

        # Process the user_message and prepare a response
        response_message = "You said: " + user_message

        alice_response = {
            "response": {
                "text": response_message,
                "end_session": False
            },
            "version": "1.0"
        }

        return JsonResponse(alice_response)

    return JsonResponse({"error": "Invalid request"})

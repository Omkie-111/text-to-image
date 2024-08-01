from django.http import JsonResponse
from .tasks import generate_image

def image_generation(request):
    """
    Initiate image generation tasks for a list of prompts and return the results as JSON.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the results of the image generation tasks.
    """
    prompts = ['A red flying dog', 'A piano ninja', 'A footballer kid']
    tasks = [generate_image.delay(prompt) for prompt in prompts]
    results = [task.get() for task in tasks]
    return JsonResponse(results, safe=False)

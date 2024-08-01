from django.conf import settings
from celery import shared_task
import os
import requests
import base64
import uuid
from .models import GeneratedImage

@shared_task
def generate_image(prompt):
    """
    Generate an image based on the given prompt using the Stability API.

    Args:
        prompt (str): The text prompt to generate the image.

    Returns:
        dict: A dictionary containing the prompt, image URL, and a success message or an error message.
    """
    try:
        response = requests.post(
            settings.STABILITY_API_URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {settings.STABILITY_API_KEY}"
            },
            json={
                "text_prompts": [{"text": prompt}],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception(f"Non-200 response: {response.text}")

        data = response.json()

        for i, image in enumerate(data["artifacts"]):
            image_path = os.path.join(settings.MEDIA_ROOT, f"txt_to_img_{uuid.uuid4()}.png")
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(image["base64"]))
            GeneratedImage.objects.create(prompt=prompt, image_url=image_path)

        return {"prompt": prompt, "image_url": image_path, "message": "Image Generated Successfully !!!"}
    
    except Exception as e:
        return {"error": str(e)}

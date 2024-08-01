## Text to Game AI

### Overview
It is a Django application that generates three images in parallel using Stability AI’s Text-to-image generation API. The project employs Celery for parallel processing to manage asynchronous calls to the API.

### Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Django Setup](#django-setup)
  - [Celery Setup](#celery-setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Generating Images](#generating-images)
- [Bonus Task](#bonus-task)
- [Resources](#resources)

### Project Structure
```
text-to-image/
├── text_to_image/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── celery.py
├── images/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── manage.py
├── README.md
├── requirements.txt
```

### Setup Instructions

#### Prerequisites
- Python 3.x
- Django 3.x or higher
- Redis server
- Celery
- Stability AI Account

#### Django Setup
1. **Create Virtual Environment**:
    ```sh
    python -m venv myvenv
    source myenv/bin/activate
    ```

2. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd text-to-image
    ```
    
3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the Django server**:
    ```sh
    python manage.py runserver
    ```

#### Celery Setup
1. **Install Redis**:
   Follow instructions for your operating system to install Redis.

2. **Configure Celery**:
   Ensure that your `text_to_image/celery.py` is properly configured:
    ```python
    from __future__ import absolute_import, unicode_literals
    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_to_image.settings')

    app = Celery('text_to_image')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
    ```

3. **Start Celery worker**:
    ```sh
    celery -A text_to_image worker --loglevel=info
    ```

### Usage

#### Running the Application
1. Ensure that the Django server and Celery worker are running.
2. Access the Django admin interface to manage and monitor tasks.

#### Generating Images
1. Make a POST request to the endpoint responsible for generating images.
2. The application will use Celery to handle the generation of three images in parallel using the Stability AI API.

### Bonus Task
To simulate storing the resulting image URLs or metadata, we can use Django models. In `models.py`, a simple model can be added:
```python
from django.db import models

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt
```

### Resources
- **Create a Stability AI Account**: Visit [Stability AI](https://stability.ai) and create an account. Upon signing up, you will receive 25 free credits.
- **API Documentation**: [Stability AI API Docs](https://platform.stability.ai/docs/api-reference#tag/Text-to-Image/operation/textToImage)
- **API Endpoint**: Use the Stable Diffusion XL Version 1 API for image generation. Note that SD3 costs 6 credits per call, so use SDXL or below for this assignment: [API URL](https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image)

Prompts for image generation:
1. A red flying dog
2. A piano ninja
3. A footballer kid

import os
import sys
import requests
from django.core.wsgi import get_wsgi_application
from django.shortcuts import render
from a_Django_app.models import Package

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_Django_project.settings')
application = get_wsgi_application()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def home(request):
    return render(request, 'home.html', {'base_template': 'a_django_app/base.html'})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def packages(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': packages})


def package_detail(request, pk):
    package = Package.objects.get(pk=pk)
    return render(request, 'package_detail.html', {'package': package})


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        api_url = 'https://w60ancsmh5.execute-api.ap-southeast-2.amazonaws.com/Prod'
        headers = {'Content-Type': 'application/json'}
        data = {'message': message}

        response = requests.post(api_url, headers=headers, json=data)
        chatbot_response = response.json()['body']['message']

        return render(request, 'chatbot.html', {'chatbot_response': chatbot_response})

    return render(request, 'chatbot.html')

# example/views.py
from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Try Django 🧑‍💻</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
# def index(request):
#     return render(request, 'notes/index.html')
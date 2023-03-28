from django.shortcuts import render


def home(request):
    return render(request, 'wayback_app/index.html')


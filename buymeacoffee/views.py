from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {}
    return render(request, 'buymeacoffee/mainpage.html', context)
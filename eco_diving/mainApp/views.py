from django.shortcuts import render

def homeView(request):
    return render(request, 'mainApp/eco_diving.html')

def projectView(request):
    return render(request, 'mainApp/project.html')

def newsView(request):
    return render(request, 'mainApp/news.html')
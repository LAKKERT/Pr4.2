from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, "home.html")
# Create your views here.
def aboutPageView(request):
    return render(request, "about.html")
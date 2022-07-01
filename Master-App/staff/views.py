from django.shortcuts import render

# Create your views here.
def start_page(request):
    context = {}
    return render(request, 'index.html', context)
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
       'name': 'Gabriella Naomi Hutagalung',
       'class': 'PBP D'
    }

    return render(request, "main.html", context)
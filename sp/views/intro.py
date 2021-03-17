from django.shortcuts import render


def intro(request):

    return render(request, 'sp/intro/view.html')

from django.shortcuts import render


def intro_view(request):

    context = {
        'is_dashboard': False,
    }

    return render(request, 'sp/intro/view.html', context)

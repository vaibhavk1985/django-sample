from django.shortcuts import render


def handler404(request, exception):
    data = {}
    return render(request, '404.html', data)


def handler500(request,  exception):
    data = {}
    return render(request, '500.html', data)

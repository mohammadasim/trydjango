from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'pages/home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'pages/contact.html', {})


def about_view(request, *args, **kwargs):
    new_user = {
        "name": "Jack",
        "age": "108 months",
        "father": "James",
        "mother": "Joana",
        "siblings": ["John", "Jamima"]

    }
    return render(request, 'pages/about.html', new_user)

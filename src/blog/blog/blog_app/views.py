from django.shortcuts import render

posts = [
    {
        'author': 'Author 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 09, 2021'
    },
    {
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 09, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})

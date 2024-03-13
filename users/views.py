from django.shortcuts import render


# Create your views here.
def user_login(request):
    # kerakli kodlari yozish kerak
    return render(request, 'auth/login.html')


def user_register(request):
    # kerakli kodlari yozish kerak
    return render(request, 'auth/register.html')

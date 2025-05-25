from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_main_menu(request):
    return render(request, 'userloginmain/user_main_menu.html')


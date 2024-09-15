from django.shortcuts import render, redirect

# Create your views here.
def chatPage(request):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request, 'chat/chatpage.html')
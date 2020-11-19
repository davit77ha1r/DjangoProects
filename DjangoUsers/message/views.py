from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return render(request, 'message/main.html')
def home_view(request):
    messages = Message.objects.all()
    users = User.objects.all()
    context = {
        "users":user,
        "messages":messages,
    }
    return request(render,"message/home.html",contex)
def user_register(request):
    if request.method == "Post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_view")
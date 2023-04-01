from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_details')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required #this  decorator is used for login authentication
def user_details(request):
    return render(request, 'user_details.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        # Save the new user object
        response = super().form_valid(form)

        # Authenticate and log the user in
        email = self.request.POST.get('email')
        password = self.request.POST.get('password1')
        try:
            mobile = self.request.POST.get('mobile')
        except Exception as e:
            return HttpResponse("Please Enter a Valid number")
        user = authenticate(self.request, email=email, password=password, mobile=mobile)
        login(self.request, user)

        return response



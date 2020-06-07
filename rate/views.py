from django.shortcuts import render,redirect
from .models import Project,Profile
from .forms import RegisterForm,ProfileForm,UpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.core.exceptions import ObjectDoesNotExist
from pyuploadcare.dj.forms import ImageField



def index(request):

    posts = Project .objects.all()

    return render(request, 'index.html', {"posts":posts})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            

            messages.success(request, f'Account {username} created')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request , 'registration/register.html', {'form':form})




@login_required
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    if request.method == 'POST':
        user_form = UpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account {username} has been updated')
            return redirect('profile')



    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)


    # try:
    #     profile = Profile.objects.get(user=current_user)
    #     posts = Image.objects.filter(account_id= current_user_id)

    # except ObjectDoesNotExist:
    #     return redirect(profile)

    context = {'user_form':user_form, 'profile_form':profile_form}


    return render(request, 'profile.html', context)





class PostView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'posts'



class DetailView(DetailView):
    model = Project
    template_name = 'detail.html'


class CreateView(LoginRequiredMixin,CreateView):
    photo = ImageField(label='post')

    model = Project
    success_url = '/'
    template_name = 'post_form.html'
    fields = [ 'title', 'description','photo','link']


    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)




class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    photo = ImageField(label='post')

    model = Project
    success_url = '/'
    template_name = 'post_form.html'
    fields = [ 'title', 'description','photo','link']



    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.account:
            return True
        return False


class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Project
    
    success_url = '/'
    template_name = 'delete.html'

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.account:
            return True
        return False
from django.shortcuts import render,redirect,HttpResponseRedirect,Http404
from .models import Project,Profile
from .forms import RegisterForm,ProfileForm,UpdateForm,VoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.core.exceptions import ObjectDoesNotExist
from pyuploadcare.dj.forms import ImageField



def index(request):

    posts = Project.objects.all()
    

    return render(request, 'index.html', {"posts":posts})



@login_required
def detail(request,project_id):
    post = Project.objects.get(id = project_id)


    try:
        post = Project.objects.get(id = project_id)
        average_score = round(((post.design + post.usability + post.content)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                post.votes+=1
                if post.design == 0:
                    post.design = int(request.POST['design'])
                else:
                    post.design = (post.design + int(request.POST['design']))/2
                if post.usability == 0:
                    post.usability = int(request.POST['usability'])
                else:
                    post.usability = (post.usability + int(request.POST['usability']))/2
                if post.content == 0:
                    post.content = int(request.POST['content'])
                else:
                    post.content = (post.content + int(request.POST['usability']))/2

                post.save()
                return redirect('detail',project_id)
        else:
            vote_form = VoteForm()

    except ObjectDoesNotExist:
        return redirect('detail',project_id)
    return render(request,'detail.html',{"vote_form":vote_form,"post":post,"average_score":average_score})






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


    try:
        profile = Profile.objects.get(user=current_user)
        posts = Project.objects.filter(account_id= current_user_id)

    except ObjectDoesNotExist:
        return redirect('profile')

    context = {'user_form':user_form, 'profile_form':profile_form}


    return render(request, 'profile.html', context)


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get('project')
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})



class PostView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'posts'






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
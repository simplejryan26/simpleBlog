from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth import authenticate, login, logout

# from django.contrib import messages

# from django.contrib.auth.decorators import login_required
# Create your views here.
# def home(request):
# 	return render(request, 'home.html', {})
class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	cats = Category.objects.all()
	# ordering = [date_created]

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()	
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

# def CategoryListView(request, cats):
# 	category_posts = Post.objects.filter(category=cats.replace('-',' '))
# 	return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog_details.html'	

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'	
	#fields = '__all__'
	

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'	
	# fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	# form_class = PostForm
	template_name = 'add_category.html'	
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	# fields = ['title', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

	
				
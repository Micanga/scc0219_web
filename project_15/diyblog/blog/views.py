from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from blog.models import Author, Blog, Comment
from django.views import generic
from django.contrib.auth.models import User #Blog author or commenter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_users = get_user_model().objects.all().count()
    num_blogs= Blog.objects.all().count() 
    num_authors = Author.objects.all().count()
    
    context = {
        'num_users': num_users,
        'num_blogs': num_blogs,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'blog.html', context=context)



class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorDetailView(generic.DetailView):
    model = Author

class BlogCommentView(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Comment
    fields = ['message']
        
    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentView, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})

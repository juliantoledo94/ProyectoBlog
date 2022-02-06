from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

from django.contrib.auth.models import User
from django.views.generic import CreateView

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name='comentaries/add_comment.html'
    
    def form_valid(self,form):  
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
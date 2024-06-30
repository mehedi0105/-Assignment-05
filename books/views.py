from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

# class DetailsPostView(DetailView):
#     model = models.Book
#     pk_url_kwarg = 'id'
#     template_name = 'post_details.html'
    
#     def post(self, request, *args, **kwargs):
#         comment_form = forms.CommentForm(data=self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#         return self.get(request, *args, **kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object # post model er object ekhane store korlam
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()
        
#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context

class DetailsPostView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'


# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id) 
#     post_form = forms.PostForm(instance=post)
#     # print(post.title)
#     if request.method == 'POST': # user post request koreche
#         post_form = forms.PostForm(request.POST, instance=post) # user er post request data ekhane capture korlam
#         if post_form.is_valid(): # post kora data gula amra valid kina check kortechi
#             post_form.instance.author = request.user
#             post_form.save() # jodi data valid hoy taile database e save korbo
#             return redirect('homepage') # sob thik thakle take add author ei url e pathiye dibo
    
#     return render(request, 'add_post.html', {'form' : post_form})


# amount = form.cleaned_data.get('amount')

#     self.request.user.account.balance -= form.cleaned_data.get('amount')
#     # balance = 300
#     # amount = 5000
#     self.request.user.account.save(update_fields=['balance'])

def Brrow_Book(request, id):
    book = models.Book.objects.get(pk=id)
    request.user.account.balance -= book.borrow_price
    
    book.borrow = True
    book.save(update_fields=['borrow'])
    print(book.borrow)

    request.user.account.save(update_fields=['balance'])
    print(book.borrow_price)
    return redirect('homepage')


class CommentPostView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'post_details1.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


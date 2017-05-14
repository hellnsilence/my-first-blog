from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def contact(request):
    form_class = ContactForm

	
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get(
				'content'
			, '')

            send_mail(
				'Response to site',
				form_content,
				contact_email,
				['bogdan.podvirny@gmail.com'],
				fail_silently=False,
			)
			
            return redirect('http://127.0.0.1:8000/', permanent=True)

    return render(request, 'blog/contact.html', {
        'form': form_class,
    })
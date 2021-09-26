from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form  = ReviewForm()

    context = {
        'form' : form,
    }
    return render(request, 'community/form.html', context)

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews,
    }
    return render(request, 'community/index.html', context)

def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review' : review,
    }
    return render(request, 'community/detail.html', context)

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form  = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form' : form,
        'review' : review,
    }
    return render(request, 'community/form.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=pk)
        review.delete()
        return redirect('community:index')
    else:
        return redirect('community:login')
from django.shortcuts import render
from feedback_app.forms import FeedbackForm
from feedback_app.models import Feedback
from django.shortcuts import redirect


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            Feedback.objects.create(
                subject=subject,
                name=name,
                email=email,
                message=message
            )

            return redirect('feedback:feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'blog/feedback_page.html', context={'form': form})


def feedback_success(request):
    return render(request, 'blog/success.html')

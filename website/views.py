from django.shortcuts import render
from jobboard.models import JobListing


def home(request):
    return render(
        request,
        "website/home.html",
        {"message": "Hello!", "job_listing_count": JobListing.objects.count()},
    )

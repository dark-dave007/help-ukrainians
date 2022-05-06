from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from .forms import DonationForm, RequestForm
from .models import Donation, Request, User

from itertools import chain
from operator import attrgetter


def index(request):
    result_list = sorted(
        chain(Request.objects.all(), Donation.objects.all()),
        key=attrgetter("date_created"),
    )
    return render(
        request,
        "web/index.html",
        {"images": result_list},
    )


@login_required(login_url="web/login.html")
def post_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            img = form.cleaned_data["img"]
            category = form.cleaned_data["category"]

            Request(
                title=title,
                description=description,
                img=img,
                category=category,
                creator=request.user,
            ).save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "web/post.html",
                {
                    "message": "Required field(s) missing.",
                    "type": "Request",
                    "url": "post_request",
                    "form": RequestForm(),
                },
            )

    return render(
        request,
        "web/post.html",
        {"type": "Request", "url": "post_request", "form": RequestForm(None)},
    )


@login_required(login_url="web/login.html")
def post_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            img = form.cleaned_data["img"]
            category = form.cleaned_data["category"]

            Donation(
                title=title,
                description=description,
                img=img,
                category=category,
                creator=request.user,
            ).save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "web/post.html",
                {
                    "message": "Required field(s) missing.",
                    "type": "Donation",
                    "url": "post_donation",
                    "form": DonationForm(),
                },
            )

    return render(
        request,
        "web/post.html",
        {"type": "Donation", "url": "post_donation", "form": DonationForm(None)},
    )


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "web/login.html",
                {"message": "Invalid email and/or password."},
            )
    else:
        return render(request, "web/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        import re

        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure valid email address
        if email and not re.match(EMAIL_REGEX, email):
            return render(
                request, "web/register.html", {"message": "Not a valid email address."}
            )

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "web/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "web/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "web/register.html")

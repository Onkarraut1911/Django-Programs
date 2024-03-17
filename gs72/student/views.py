from django.shortcuts import render


# Create your views here.
def setsession(request):
    request.session["name"] = "sonam"
    request.session["lname"] = "jha"
    request.session.set_expiry(
        600
    )  # this is in seconds , if we set 0 then its expiry at browser close
    return render(request, "student/setsession.html")


def getsession(request):
    name = request.session["name"]
    return render(request, "student/getsession.html", {"name": name})


def delsession(request):
    request.session.flush()  # this is delete all the session data
    request.session.clear_expired()  # this is clear the session in the database
    return render(request, "student/delsession.html")

from django.shortcuts import render


# Create your views here.
def setsession(request):
    request.session["name"] = "sonam"
    request.session["lname"] = "jha"

    return render(request, "student/setsession.html")


def getsession(request):
    # name = request.session["name"]
    name = request.session.get("name", default="guest")
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault(
        "age", "26"
    )  # this is set the value also get the value
    return render(
        request,
        "student/getsession.html",
        {"name": name, "keys": keys, "items": items, "age": age},
    )


def delsession(request):
    # if "name" in request.session:
    #     del request.session["name"]   # this is delete perticulare value
    request.session.flush()  # this is delete all the session data
    return render(request, "student/delsession.html")

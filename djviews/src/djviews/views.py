from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
#     return HttpResponse("<h1> hello there </h1>")


def home(request):
    response = HttpResponse()
    response.write("<p>hi there</p>")
    print(response.status_code)
    response.status_code = 200
    return response
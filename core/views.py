from django.http import HttpResponse


# Create your views here.


def square_of_a(request):
    a = request.GET.get("a")
    if str(a).isdigit():
        return HttpResponse(content=f"Aaa in square is {int(a) ** 2}")
    return HttpResponse(content=f"Aaa is not a digit, or not presented")

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # data={
    #     "title": "Newsletter sign-up form with success message",
    #     "stay":"Stay updated!",
    #     "sub":["comp","science","math"],
    #     "tableka":[
    #         {"name":"rahul","phoneno":9348325249},
    #         {"name":"kraj","phoneno":8455030029},
    #         {"name":"bramha","phoneno":7077584491}
    #     ],
    #     "numbers":[1,2,3,4,5,6,2,6]
    # }
    return render(request,"index.html")

def page(request):
    return render(request,"page.html")

def course(request):
    return HttpResponse("Edhar sare course bikte hai")

def coursedetails(request,courseid):
    return HttpResponse(courseid)
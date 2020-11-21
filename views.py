from django.shortcuts import render

import requests
#import pyfiglet
#import termcolor
from random import choice

# Create your views here.
def home(request):

    return render(request,"home.html")


def find(request):
    joke=request.GET['string']


    #header = pyfiglet.figlet_format("Dad Joke 3000")
    #header = termcolor.colored(header, color="magenta")
    #print(header)
    user_input=joke

    response_json=requests.get("https://icanhazdadjoke.com/search",
                           headers={"Accept":"application/json"},
                           params={"term":user_input}).json()

    nums_jokes=response_json['total_jokes']
    result=response_json["results"]

    if nums_jokes>1:

        return render(request,"home.html",{'result':"{}".format(choice(result)["joke"])})

    elif nums_jokes==1:

        return render(request,"home.html",{'result':" "+ result[0]["joke"]})

    else:
        #print("Sorry there is no joke on this topic:(")
        return render(request,"home.html",{'result':"Sorry there is no joke on this topic:|"})

    #return render(request,"home.html",{'result':""})
    return

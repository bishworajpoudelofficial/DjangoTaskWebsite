from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_task = {
    'january':'Publish Learn AI App on Store.',
    'feb': 'Teach AI Class In US',
    'march': 'Publish One Other App',
    'april': 'Teach AI Class In India',
    'may': 'Publish One Other App',
    'june': 'Teach AI Class In US',
    'july': 'Publish One Other App',
    'august': 'Teach AI Class In India',
    'september': 'Publish One Other App',
    'october': 'Teach AI Class In US',
    'november': 'Publish One Other App',
    'december': 'Teach AI Class In India',
}

def home(request):
    return render(request,"monthlyapp/index.html",{
        'keys':  list(monthly_task.keys()),
        'values': list(monthly_task.values())
    })
    # all_items = """
    # <h1> My Monthly Plan </h1>
    # """
    # months = list(monthly_task.keys())
    
    # for month in months:
    #     all_items = all_items + f"<li> <a href='/{month}'>{month.capitalize()}</a></li>"
    # return HttpResponse(all_items)    

def index(request,month):
        work = monthly_task[month]
        return render(request, "monthlyapp/work.html",{
            'month': month,
            "plan": work
        })


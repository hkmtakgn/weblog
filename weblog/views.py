from django.shortcuts import render

def weblog_home_views (request):
    context = dict ()
    return render (request, "main_pages/weblog-home.html", context)



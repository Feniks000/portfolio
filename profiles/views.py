from django.shortcuts import render, Http404

def show_reg(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        raise Http404
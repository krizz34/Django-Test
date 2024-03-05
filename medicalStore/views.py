from django.shortcuts import render, redirect
from .models import medic
from .forms import medicForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required



def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'page_Tsignup/signUp.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    else:
        form = AuthenticationForm()

    return render(request, 'page_Tlogin/login.html', {'form': form})

@login_required(login_url='/login/')
def userLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context = {
        'user': request.user
    }   
    return render(request, 'page_Tlogout/logout.html', context)








@login_required(login_url='/login/')
def home(request):
    return render(request, 'page_default/default.html')

@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = medicForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('readData')
    else:
        form = medicForm()
    return render(request, 'page_create/createForm.html', {'form': form})

@login_required(login_url='/login/')
def read(request):
    medicData = medic.objects.all()
    return render(request,'page_read/readData.html',{'medicData': medicData})

@login_required(login_url='/login/')
def update(request, pk):
    item = medic.objects.get(pk=pk)
    if request.method == 'POST':
        form = medicForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('readData')
    else:
        form = medicForm(instance= item)
    return render(request, 'page_update/updateForm.html', {'form': form})

@login_required(login_url='/login/')
def delete(request, pk):
    item = medic.objects.get(pk=pk)
    if request.method == 'POST':
            item.delete()
            return redirect('readData')
    return render(request, 'page_delete/deleteForm.html', {'medic_name': item.Mname})


@login_required(login_url='/login/')
def contactus(request):
    return render(request,'page_contactus/contactus.html')

@login_required(login_url='/login/')
def aboutus(request):
    return render(request,'page_aboutus/aboutus.html')


@login_required(login_url='/login/')
def search(request):
    if 'search_term' in request.GET:
        search_term = request.GET['search_term']
        matching_medicines = medic.objects.filter(Mname__istartswith=search_term)
        return render(request, 'page_search/search.html', {'matching_medicines': matching_medicines, 'search_term': search_term})
    return render(request, 'page_search/search.html', {'matching_medicines': None})

# def search(request):
#     medicData = medic.objects.all()
#     nameDict = {}
#     for item in medicData:
#         nameDict = appe

#     return render(request,'page_read/readData.html',{'medicData': medicData})


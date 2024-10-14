from django.shortcuts import render,redirect
from .models import User, Note
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
            return HttpResponse("Already exists")
        else:
            hashed_password=make_password(password)
            User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed_password)
            return redirect('login')
    return render(request,'register.html')

def login(request):
    config={}
    if 'user' in request.session:
        return redirect('create_notes')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            if check_password(password,user.password):
                request.session['user']={
                    'id':user.id,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email
                        }
                return redirect('create_notes')
        except:
            config['errors']="Invalid email or password"
    return render(request,'login.html',config)

def create_notes(request):
    user_info=request.session['user']
    user_id=user_info['id']
    user_instance=User.objects.get(id=user_id)
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        if title:
            if Note.objects.filter(title=title,user=user_instance).exists():
                return HttpResponse('Already exists')
            else:
                Note.objects.create(title=title,content=content,user=user_instance)
                return redirect('notes_list')
    return render(request,'create_notes.html',{'user_info':user_info})

def notes_list(request):
    user_info=request.session['user']
    user_id=user_info['id']
    user_instance=User.objects.get(id=user_id)
    user_notes=Note.objects.filter(user=user_instance)
    return render(request,'notes_list.html',{'user_info':user_info,'user_notes':user_notes})

def update_and_save(request,note_id):
    user_info=request.session['user']
    user_id=user_info['id']
    user_instance=User.objects.get(id=user_id)
    note=Note.objects.get(id=note_id)
    if request.method=='POST':
        updated_title=request.POST.get('title')
        updated_content=request.POST.get('content')
        if updated_title:
            note.title=updated_title
        if updated_content:
            note.content=updated_content
        note.save()
        return redirect('notes_list')
    return render(request,'update_notes_list.html',{'note':note})

def delete_note(request,note_id):
    Note.objects.get(id=note_id).delete()
    return redirect('notes_list')

def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('login')
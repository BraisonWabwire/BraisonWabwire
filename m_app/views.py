from django.shortcuts import render
from django.http import request,HttpResponseRedirect,HttpResponse
from .forms import StudentForm,studSignupform,studentFileForm
from .functions import handle_uploaded_file

# Create your views here.
def index(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            form=StudentForm()
            return HttpResponseRedirect('/thanks/')
    else:
     form=StudentForm()
     context={'form':form}
    return render(request, 'index.html', context)

def thanks(request):
   return render(request,'thanks.html')


def signup(request):
    if request.method == 'POST':
        form = studSignupform(request.POST)
        if form.is_valid():
            # Save the form data
            new_student = form.save()
            
            # Store data in session
            request.session['student_id'] = new_student.id
            request.session['student_name'] = f"{new_student.f_name} {new_student.l_name}"
            
            # Clear the form after saving
            form = studSignupform()
            
            # Redirect to a 'thanks' page or another URL
            return HttpResponseRedirect('/thanks/')
    else:
        form = studSignupform()
    
    context = {'form': form}
    return render(request, 'signup.html', context)

def studUpload(request):
    if request.method == 'POST':
        form = studentFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['certificate'])  # Assuming the file field is named 'certificate'
            form.save()
            return HttpResponse("File uploaded successfully!")
    else:
        form = studentFileForm()

    context = {'form': form}
    return render(request, 'upload.html', context)


def visits(request):
    request.session['visit']=int(request.session.get('visit,0'))+1



         
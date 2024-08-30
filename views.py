from django.shortcuts import render, redirect
from. models import *
from keras.models import Model, Sequential, load_model
import numpy as np
from keras.preprocessing import image
# Create your views here.



def index (request):
    return render(request, "index.html")

def base (request):
    return render(request, "base.html")

def about (request):
    return render(request, "about.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email1 = request.POST['mail']
        aage = request.POST['age']
        add = request.POST['add']
        password = request.POST['passw']
        confirmpassword = request.POST['cpassw']
        if password == confirmpassword:
            # Create an instance of the Register model
            a = Register(name=uname, email=email1, password=password, age=aage, address=add)
            a.save()
            msg = "Successfully Registered"
            return render(request, 'login.html', {"msg": msg})
        mssg = "Registration Failed, Try Again"

        return render(request, "register.html", {'msg': mssg})
    return render(request, "register.html")


def logins(request):
    if request.method=='POST':
        email=request.POST['lmail']
        password=request.POST['lpassw']
        d=Register.objects.filter(email=email, password=password).exists()

        print(d)
        print(email)
        print(password)
        if d:
            return redirect(upload)
        else:
            h="login failed"
            return render(request,"login.html",{"msg":h})
    return render(request,"login.html")


def upload(request):
    pathss = os.listdir(r"app/Dataset/test/")
    classes = []

    for i in pathss:
        classes.append(i)

    if request.method == 'POST':
        file = request.FILES['hop']
        img = Cardio(image=file)
        img.save()
        path = "app/static/saved/" + img.filename()
        path1 = "/static/saved/" + img.filename()
        m=int(request.POST['alg'])
        if m==1:
            models = load_model("app/models/MOBILENET.h5")

        if m==2:
            models = load_model("app/models/VGG19Model.h5")

        x = image.load_img(path, target_size=(224, 224))
        x = image.img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x /= 255
        results = models.predict(x)
        b = np.argmax(results)
        prediction = classes[b]
        if prediction=="true":
            resultmsg="The results show that your heart is enlarged, a condition called cardiomegaly"
        else:
            resultmsg="The tests show that you don't have cardiomegaly, which means your heart is not enlarged"
        return render(request,"result.html",{"res":prediction,"path":path1, "rn":resultmsg})

    return render(request, "upload.html") 

def result(request):
    return render(request, "result.html")

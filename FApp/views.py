from django.shortcuts import render, redirect
from FApp.models import Category_Db ,Product_Db

from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from newapp.models import ContactDb

from django.contrib import messages

# Create your views here.
def indexpage(request):
    cat=Category_Db.objects.count()
    pro=Product_Db.objects.count()
    return render(request , "index.html",{'cat':cat,'pro':pro})

def add_category(request):
    return render(request,"addcategory.html")

def save_category(request):
    if request.method == "POST":
        category = request.POST.get('cname')
        des = request.POST.get('description')
        image = request.FILES['img']

        obj = Category_Db(category_name=category , description=des , category_image=image)
        obj.save()
        messages.success(request,"Category saved..!")
        return redirect(add_category)
def view_category(request):
    data = Category_Db.objects.all()
    return render(request,"viewcategory.html",{'data':data})

def edit_category(req,c_id):
    c = Category_Db.objects.get(id=c_id)
    return render(req,"editcategory.html",{'c':c})

def update_category(request,c_id):
    if request.method == "POST":
        category=request.POST.get('cname')
        des=request.POST.get('description')
        try:
            im=request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Category_Db.objects.get(id=c_id).category_image
        Category_Db.objects.filter(id=c_id).update(category_name=category,description=des,category_image=file)
        messages.success(request,"Updated successfully..!")
        return redirect(view_category)

def delete_category(req,c_id):
    x = Category_Db.objects.filter(id=c_id)
    x.delete()
    messages.error(req,"Data deleted..!")
    return redirect(view_category)



def add_product(request):
    c=Category_Db.objects.all()
    return render(request,"addproduct.html",{'c':c})

def save_product(request):
    if request.method == "POST":
        cat = request.POST.get('pcname')
        product = request.POST.get('pname')
        quantity = request.POST.get('quantity')
        mrp = request.POST.get('mrp')
        description = request.POST.get('des')
        country = request.POST.get('country')
        manufactured = request.POST.get('manu')
        image = request.FILES['img1']
        images = request.FILES['img2']
        img = request.FILES['img3']

        obj = Product_Db(category=cat,product_name=product,quantity=quantity,mrp=mrp,description=description,country=country,manufactured=manufactured,image1=image,image2=images,image3=img)
        obj.save()
        messages.success(request,"Product saved..!")
        return redirect(add_product)


def view_product(request):
    data = Product_Db.objects.all()
    return render(request,"viewproduct.html",{'data':data})



def edit_product(req,c_id):
    c=Category_Db.objects.all()
    data=Product_Db.objects.get(id=c_id)
    return render(req,"editproduct.html",{'data':data,'c':c})

def update_product(request,c_id):
    if request.method == "POST":
        cat = request.POST.get('pcname')
        product = request.POST.get('pname')
        quantity = request.POST.get('quantity')
        mrp = request.POST.get('mrp')
        description = request.POST.get('des')
        country = request.POST.get('country')
        manufactured = request.POST.get('manu')
        try:
            im=request.FILES['img1']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Product_Db.objects.get(id=c_id).image1

        try:
            im1=request.FILES['img2']
            fs=FileSystemStorage()
            file1=fs.save(im1.name,im1)
        except MultiValueDictKeyError:
            file1 = Product_Db.objects.get(id=c_id).image2

        try:
            im3 = request.FILES['img3']
            fs = FileSystemStorage()
            file2 = fs.save(im3.name, im3)
        except MultiValueDictKeyError:
            file2 = Product_Db.objects.get(id=c_id).image3

        Product_Db.objects.filter(id=c_id).update(category=cat,product_name=product,quantity=quantity,mrp=mrp,
                                                   description=description,country=country,manufactured=manufactured,
                                                   image1=file,image2=file1,image3=file2)

        messages.success(request,"Updated successfully..!")
        return redirect(view_product)



def delete_product(req,c_id):
    x = Product_Db.objects.filter(id=c_id)
    x.delete()
    messages.error(req,"Data deleted..!")
    return redirect(view_product)

def login_page(request):
    return render(request,"login.html")

def admin_login(request):
    if request.method == "POST":
        un=request.POST.get('username')
        ps=request.POST.get('pass')

        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=ps
                messages.success(request,"Welcome..!")
                return redirect(indexpage)
            else:
                messages.error(request, "Please check your Password")
                return redirect(login_page)
        else:
            messages.warning(request, "Invalid Username")
            return redirect(login_page)





def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request,"Logout..!")

    return redirect(login_page)


def contactdetails(request):
    c=ContactDb.objects.all()
    return render(request,"contactdetails.html",{'c':c})
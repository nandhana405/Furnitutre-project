from django.shortcuts import render,redirect

from FApp.models import Product_Db,Category_Db
from newapp.models import ContactDb,SignupDb,CartDb,orderDb

from django.contrib import messages

import razorpay

# Create your views here.


def homepage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()
    cat=Category_Db.objects.all()
    return render(request,"home.html",{'cat':cat,'car':car})


def productpage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()
    pro=Product_Db.objects.all()
    return render(request,"products.html",{'pro':pro,'car':car})


def aboutpage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()

    return render(request,"about.html",{'car':car})

def contactpage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()
    return render(request,"contact.html",{'car':car})

def savecontact(request):
    if request.method == "POST":
        first = request.POST.get('fname')
        last = request.POST.get('lname')
        mail = request.POST.get('email')
        message = request.POST.get('msg')

        obj=ContactDb(First_name=first,Last_name=last,Email=mail,Message=message)
        obj.save()
        return redirect(contactpage)


def shoppage(request,cat_name):
    data=Product_Db.objects.filter(category=cat_name)
    return render(request,"shop.html",{'data':data})

def singleproduct(request,pro_id):
    data=Product_Db.objects.get(id=pro_id)
    return render(request,"singleproduct.html",{'data':data})


def blogpage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()
    return render(request,"blog.html",{'car':car})

def signuppage(request):
    ca = CartDb.objects.filter(username=request.session['Name'])
    car = ca.count()
    return render(request,"signup.html",{'car':car})

def signinpage(request):
    return render(request,"signin.html")

def save_signup(request):
    if request.method == "POST":
        name=request.POST.get("name")
        mail=request.POST.get("email")
        mobile=request.POST.get("mobile")
        passwrd1=request.POST.get("pass")
        passwrd2=request.POST.get("re_pass")


        obj=SignupDb(Name=name,Mail=mail,Mobile=mobile,Pass1=passwrd1,Pass2=passwrd2)

        if SignupDb.objects.filter(Name=name).exists():
            messages.warning(request,"User already exists..!")
            return redirect(signuppage)
        elif SignupDb.objects.filter(Mail=mail).exists():
            messages.warning(request,"Mail ID already exists..!")
            return redirect(signuppage)


        obj.save()
        messages.success(request,"Sign in Successfull")
        return redirect(signinpage)

def Userlogin(request):
    if request.method=="POST":
        un=request.POST.get("your_name")
        pas=request.POST.get("your_pass")
        if SignupDb.objects.filter(Name=un,Pass1=pas).exists():
            request.session['Name']=un
            request.session['Pass1']=pas
            messages.success(request, "Welcome..!")
            return redirect(homepage)
        else:
            messages.error(request, "Please check your Password")
            return redirect(signinpage)
    else:
        messages.warning(request, "Invalid Username")
        return redirect(signinpage)

def Userlogout(request):
    del request.session['Name']
    del request.session['Pass1']
    messages.error(request,"LogOut...!")
    return redirect(signinpage)

def save_cart(request):
    if request.method == "POST":
        user= request.POST.get("username")
        product= request.POST.get("productname")
        Totalprice= request.POST.get("total")
        price= request.POST.get("price")
        quantity= request.POST.get("quantity")
        try:
            file=Product_Db.objects.get(product_name=product)
            img=file.image1
        except Product_Db.DoesNotExist:
            img=None

        obj=CartDb(username=user,productname=product,totalprice=Totalprice,quantity=quantity,price=price,image=img)
        obj.save()
        messages.success(request,"Saved to cart..!")
        return redirect(homepage)

def cartpage(request):
    ca=CartDb.objects.filter(username=request.session['Name'])

    car = ca.count()
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for i in ca:
        subtotal = subtotal + i.totalprice

        if subtotal>50000:
            shipping_amount =100
        else:
            shipping_amount= 250

        total_amount=shipping_amount+subtotal
    return render(request,"cart.html",{'ca':ca,'subtotal':subtotal,
                                       'shipping_amount':shipping_amount,'total_amount':total_amount,'car':car})

def deletecart(request,d_id):
    x=CartDb.objects.filter(id=d_id)
    x.delete()
    return redirect(cartpage)

def chechoutpage(request):
    ca=CartDb.objects.filter(username=request.session['Name'])
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for i in ca:
        subtotal = subtotal + i.totalprice

        if subtotal > 50000:
            shipping_amount = 100
        else:
            shipping_amount = 250

        total_amount = shipping_amount + subtotal
    return render(request,"checkout.html",{'ca':ca,'subtotal':subtotal,
                                       'shipping_amount':shipping_amount,'total_amount':total_amount})


def save_order(request):
    if request.method == "POST":
        Name= request.POST.get("name")
        Mail= request.POST.get("mail")
        Totalprice= request.POST.get("total")
        Place= request.POST.get("place")
        Address= request.POST.get("address")
        Mobile= request.POST.get("mobile")
        Message= request.POST.get("message")

        obj=orderDb(name=Name,mail=Mail,total_price=Totalprice,place=Place,address=Address,mobile=Mobile,message=Message)
        obj.save()

        return redirect(paymentpage)


def paymentpage(request):
    # Retrive the data from orderDb with the specified ID
    customer = orderDb.objects.order_by('-id').first()

    #Get the payment amount of the specified  customer
    pay =customer.total_price

    #convert the amount into paisa (smallest currency unit)
    amount = int(pay*100)   #Assuming the payment amount in rupees

    pay_str = str(amount)
    

    for i in pay_str:
        print(i)

    if request.method=="POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_mg4QhrcnLZxkwq','fIVFhjtRMXs7A1U2JZnZyoYE'))
        payment = client.order.create({'currency':order_currency,'amount':amount})



    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})


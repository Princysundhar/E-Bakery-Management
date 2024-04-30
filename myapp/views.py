import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def log(request):
    return render(request,"login_index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"
        if data.type == 'admin':
            return HttpResponse("<script>alert('Welcome to Admin Home');window.location='/admin_home'</script>")
        else:
            return HttpResponse("<script>alert('Welcome to User Home');window.location='/user_home'</script>")
    else:
        return HttpResponse("<script>alert('Invalid Authentication');window.location='/'</script>")


def admin_home(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")

    return render(request,"Admin/admin_index.html")

def user_home(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"User/user_index.html")

def logout(request):
    request.session['lg'] = ""
    return HttpResponse("<script>alert('Logout Successfully');window.location='/'</script>")


def forgot_password(request):
    return render(request,"forgot_password.html")

def forgot_password_post(request):
    email = request.POST['textfield']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("demo@gmail.com", "tcap lzzh lmrz afio")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "demo@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for E-Bakery Management System"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password sended');window.location='/'</script>")
    return HttpResponse("mail incorrect")

# ========== CATEGORY MANAGEMENT ==============================================================================

def add_category(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    request.session['head'] = "CATEGORY MANAGEMENT"
    return render(request,"Admin/add_category.html")

def add_category_post(request):
    category_name = request.POST['textfield']
    obj = category()
    obj.category_name = category_name
    obj.save()
    return HttpResponse("<script>alert('Category Added');window.location='/add_category'</script>")

def view_category(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = category.objects.all()
    return render(request,"Admin/view_category.html",{"data":data})

def delete_category(request,id):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Category Removed');window.location='/view_category'</script>")


# ================ PRODUCT MANAGEMENT ==========================

def add_product(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = category.objects.all()
    return render(request,"Admin/add_product.html",{"data":data})

def add_product_post(request):
    category_name = request.POST['select']
    name = request.POST['textfield']
    image = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\E_Bakery\myapp\static\product_images\\" + dt + '.jpg',image)
    path = '/static/product_images/' + dt + '.jpg'
    price = request.POST['textfield2']
    date = request.POST['textfield3']
    obj = product()
    obj.CATEGORY_id = category_name
    obj.name = name
    obj.image = path
    obj.price = price
    obj.product_date = date
    obj.save()
    return HttpResponse("<script>alert('Product Added');window.location='/add_product'</script>")

def view_product(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = product.objects.all()
    return render(request,"Admin/view_product.html",{"data":data})

def edit_product(request,id):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = product.objects.get(id=id)
    data1 = category.objects.all()
    return render(request,"Admin/Edit_product.html",{"data":data,"data1":data1})

def edit_product_post(request,id):
    try:
        category_name = request.POST['select']
        name = request.POST['textfield']
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\E_Bakery\myapp\static\product_images\\" + dt + '.jpg', image)
        path = '/static/product_images/' + dt + '.jpg'
        price = request.POST['textfield2']
        date = request.POST['textfield3']
        product.objects.filter(id=id).update(CATEGORY_id = category_name,name = name,image = path,price = price,product_date = date)
        return HttpResponse("<script>alert('Product Updated');window.location='/view_product'</script>")
    except Exception as e:
        category_name = request.POST['select']
        name = request.POST['textfield']
        price = request.POST['textfield2']
        date = request.POST['textfield3']
        product.objects.filter(id=id).update(CATEGORY_id=category_name, name=name, price=price,product_date=date)
        return HttpResponse("<script>alert('Product Updated');window.location='/view_product'</script>")


def delete_product(request,id):
    product.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Product Removed');window.location='/view_product'</script>")

def view_user(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = user.objects.all()
    return render(request,"Admin/view_user.html",{"data":data})

def change_password(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"Admin/change_password.html")

def change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    data = login.objects.filter(password=old_password,id=request.session['lid'])
    if data.exists():
        if new_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=confirm_password)
            return HttpResponse("<script>alert('Password Updated');window.location='/change_password'</script>")
        else:
            return HttpResponse("<script>alert('Password Mismatch');window.location='/change_password'</script>")

    else:
        return HttpResponse("<script>alert('Error');window.location='/change_password'</script>")



def view_complaint(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = complaint.objects.all()
    return render(request,"Admin/view_complaint.html",{"data":data})

def send_reply(request,id):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"Admin/send_reply.html",{"id":id})

def send_reply_post(request,id):
    reply = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply=reply,reply_date = datetime.datetime.now().date())
    return HttpResponse("<script>alert('Success');window.location='/view_complaint'</script>")

def view_feedback(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = feedback.objects.all()
    return render(request,"Admin/view_feedback.html",{"data":data})

def view_request_from_user(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = requests.objects.filter(status='pending')
    return render(request,"Admin/view_request_from_user.html",{"data":data})

def accept_request(request,id):
    requests.objects.filter(id=id).update(status='accept')
    return HttpResponse("<script>alert('Request Accepted');window.location='/view_request_from_user'</script>")

def reject_request(request,id):
    requests.objects.filter(id=id).update(status='reject')
    return HttpResponse("<script>alert('Request Rejected');window.location='/view_request_from_user'</script>")

def view_verified_request(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = requests.objects.filter(status='accept')
    return render(request,"Admin/verified_request.html",{"data":data})

def view_payment_report(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = requests.objects.all()
    return render(request,"Admin/view_payment_report.html",{"data":data})



# ============================= USER MODULE =======================================

def user_register(request):
    return render(request,"User_registration.html")

def user_register_post(request):
    name = request.POST['textfield']
    password = request.POST['textfield2']
    place = request.POST['textfield3']
    email = request.POST['textfield4']
    contact = request.POST['textfield5']
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('User Already Exists');window.location='/'</script>")
    else:
        obj = login()
        obj.username = email
        obj.password = password
        obj.type = 'user'
        obj.save()

        obj1 = user()
        obj1.name = name
        obj1.email = email
        obj1.contact = contact
        obj1.place = place
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('Success');window.location='/'</script>")

def view_profile(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = user.objects.get(LOGIN=request.session['lid'])
    return render(request,"User/view_profile.html",{"data":data})

def user_view_category(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = category.objects.all()
    return render(request,"User/view_category.html",{"data":data})

def user_change_password(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"User/change_password.html")

def user_change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    data = login.objects.filter(password=old_password,id=request.session['lid'])
    if data.exists():
        if new_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=confirm_password)
            return HttpResponse("<script>alert('Password Updated');window.location='/user_change_password'</script>")
        else:
            return HttpResponse("<script>alert('Password Mismatch');window.location='/user_change_password'</script>")

    else:
        return HttpResponse("<script>alert('Error');window.location='/user_change_password'</script>")

def user_view_product(request,id):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = product.objects.filter(CATEGORY=id)
    return render(request,"User/view_product.html",{"data":data})



def send_complaint(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"User/send_complaint.html")

def send_complaint_post(request):
    complaints = request.POST['textarea']
    obj = complaint()
    obj.complaints = complaints
    obj.date = datetime.datetime.now().date()
    obj.reply = 'pending'
    obj.reply_date = 'pending'
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('success');window.location='/send_complaint'</script>")

def view_reply(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = complaint.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,"User/view_reply.html",{"data":data})

def send_feedback(request):
    return render(request,"User/send_feedback.html")

def send_feedback_post(request):
    feedbacks = request.POST['textarea']
    obj = feedback()
    obj.feedbacks =feedbacks
    obj.date = datetime.datetime.now().date()
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('success');window.location='/send_feedback'</script>")



# ================================ CART =============================================

def add_to_cart(request,id):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    return render(request,"User/add_to_cart.html",{"id":id})


def add_to_cart_post(request,id):
    quantity = request.POST['textfield']
    data = cart.objects.filter(USER__LOGIN=request.session['lid'],PRODUCT=id)
    if data.exists():
        return HttpResponse("<script>alert('Product Already in Cart!!');window.location='/user_view_category'</script>")
    else:
        obj = cart()
        obj.quantity = quantity
        obj.PRODUCT_id = id
        obj.USER = user.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added to cart');window.location='/user_view_category'</script>")

def view_cart(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = cart.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,"User/view_cart.html",{"data":data})

def place_order(request,id):
    data = cart.objects.filter(USER__LOGIN=request.session['lid'])
    amount = 0
    for i in data:
        product_amount = i.PRODUCT.price
        quantity = i.quantity
        amount = int(quantity) * int(product_amount)

    if data.exists():

        obj = requests()
        obj.date = datetime.datetime.now().date()
        obj.status = 'pending'
        obj.payment_status = 'pending'
        obj.payment_date = 'pending'
        obj.USER = user.objects.get(LOGIN=request.session['lid'])
        obj.amount = amount
        obj.save()

        for i in data:
            obj1 = request_sub()
            obj1.request_date = datetime.datetime.now().date()
            obj1.quantity = i.quantity
            obj1.REQUESTS = obj
            obj1.save()
            cart.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Order Placed');window.location='/view_cart'</script>")

def view_order(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = requests.objects.filter(USER__LOGIN=request.session['lid'],status='accept',payment_status='pending',payment_date='pending')
    return render(request,"User/view_order.html",{"data":data})

def cancel_order(request,id):
    requests.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Order Cancelled');window.location='/view_cart'</script>")

#===================== PAYMENT =====================================

def payment_mode(request,rid):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = requests.objects.get(id=rid)
    request.session['orginalamount'] = data.amount
    request.session['requestid'] = rid
    return render(request,"User/payment_mode.html",{"rid":rid})

def payment_mode_post(request,rid):
    mode = request.POST['RadioGroup1']
    data1 = requests.objects.filter(id=rid)
    if mode == 'offline':
        data1.update(payment_status=mode,payment_date = datetime.datetime.now().date())
        return HttpResponse("<script>alert('Offline Payment');window.location='/view_order'</script>")
    else:
        import razorpay

        razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
        razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

        razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

        amount = float(data1[0].amount) * 100
        # amount = float(amount)

        # Create a Razorpay order (you need to implement this based on your logic)
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
            'payment_capture': '1',  # Auto-capture payment
        }

        # Create an order
        order = razorpay_client.order.create(data=order_data)

        # context = {
        #     'razorpay_api_key': razorpay_api_key,
        #     'amount': order_data['amount'],
        #     'currency': order_data['currency'],
        #     'order_id': order['id'],
        #     'rid': rid
        # }

        return render(request, 'User/UserPayProceed.html', {'razorpay_api_key': razorpay_api_key,
                                                            'amount': order_data['amount'],
                                                            'currency': order_data['currency'],
                                                            'order_id': order['id'],
                                                            'rid': rid
        })


def on_payment_success(request,id):
    dt = datetime.datetime.now().date()
    requests.objects.filter(id=id).update(payment_status='online',payment_date=dt)
    return HttpResponse("<script>alert('Success!');window.location='/view_order'</script>")



def view_purchase_history(request):
    if "lid" not in request.session:
        return HttpResponse("<script>alert('Session expired!Login again');window.location='/'</script>")
    data = request_sub.objects.filter(Q(REQUESTS__payment_status='online')|Q(REQUESTS__payment_status='offline'),REQUESTS__USER__LOGIN=request.session['lid'],REQUESTS__status='accept')
    return render(request,"User/view_purchase_history.html",{"data":data})


from django.shortcuts import redirect, render
from lists.models import Item, Pd, Pp, E, I, R, WE

def home_page(request):
    items = Pd.objects.all()
    itemsPp = Pp.objects.all()
    # itemsE = E.objects.all()
    if len(items) == 0:
        pd=None
    else:
        pd = items[0]

    if len(itemsPp) ==0 :
        pp = None
    else:
        pp = itemsPp[0]
    # e = itemsE[0]
    e = E.objects.all()
    i = I.objects.all()
    r = R.objects.all()
    w = WE.objects.all()
    return render(request, 'home.html', {'pd': pd, 'pp': pp, 'e' : e, 'i' : i, 'r' : r, 'w' : w})

def save_pd(request):
    if request.method == 'POST':
        # print("intra")
        lst=Pd.objects.all()
        # Item.objects.create(text=request.POST['save_pd'])
        if len(lst) == 0:
            name=request.POST['name_pd']
            email = request.POST['email_pd']
            phone_number = request.POST['phone_pd']
            adress = request.POST['adress_pd']
            p = Pd.objects.create(name=name, email=email, phone_number=phone_number, adress=adress)
            p.save()
        else:
            lst[0].name=request.POST['name_pd']
            lst[0].email=request.POST['email_pd']
            lst[0].phone_number= request.POST['phone_pd']
            lst[0].adress=request.POST['adress_pd']
            lst[0].save()
            # name = request.POST['name_pd']
            # email = request.POST['email_pd']
            # phone_number = request.POST['phone_pd']
            # adress = request.POST['adress_pd']
        
        
        # print("REQUEST")
        print(request.POST)
    return redirect('/')
    
def save_pp(request):
    if request.method == 'POST':
        print("intra")
        lst2=Pp.objects.all()
        if len(lst2) == 0:
            description = request.POST['description_pp']
            d=Pp.objects.create(description=description)
            d.save()
        else:
            lst2[0].description=request.POST['description_pp']
            lst2[0].save()
        print("REQUEST")
        print(request.POST)


    return redirect('/')

def save_e(request):
    if request.method =='POST':
            school = request.POST['school_e']
            subject = request.POST['subject_e']
            start = request.POST['start_e']
            end = request.POST['end_e']
            u = E.objects.create(school= school, subject=subject, start=start, end=end)
            u.save()
            print(request.POST)
    return redirect('/')

def edit_e(request):
    if request.method =='POST':
        print(request.POST)
        id = request.POST['id_e']
        elem = E.objects.all()[int(id) - 1]
        print(elem)
        elem.school = request.POST['school_edit_e']
        elem.subject = request.POST['subject_edit_e']
        elem.start = request.POST['start_edit_e']
        elem.end = request.POST['end_edit_e']
        elem.save()
        print(request.POST)
    return redirect('/')

def save_i(request):
    if request.method =='POST':
        interest= request.POST['interests_i']
        i2= I.objects.create(interest= interest)
        i2.save()
        print(request.POST)
    return redirect('/')

def edit_i (request):
    if request.method =='POST':
        idI = request.POST['id_i']
        elemI = I.objects.all()[int(idI) - 1]
        elemI.interest = request.POST['interests_edit_i']
        elemI.save()
        print(request.POST)
    return redirect('/')


def save_r (request):
    if request.method =='POST':
        name = request.POST['nameRef_r']
        phone = request.POST['phoneRef_r']
        email = request.POST['emailRef_r']
        i3 = R.objects.create(name=name, phone=phone, email=email)
        i3.save()
        print(request.POST)
    return redirect('/')

def edit_r (request):
    if request.method == 'POST':
        idR = request.POST['id_r']
        elemR = R.objects.all()[int(idR) - 1]
        elemR.name = request.POST['nameRef_edit_r']
        elemR.phone = request.POST['phoneRef_edit_r']
        elemR.email = request.POST['emailRef_edit_r']
        elemR.save()
        print(request.POST)
    return redirect('/')

def save_we (request):
    if request.method == 'POST':
        company = request.POST['company_we']
        job = request.POST['job_we']
        description = request.POST['description_we']
        i4 = WE.objects.create(company=company, job=job, description= description)
        i4.save()
        print(request.POST)
    return redirect('/')

def edit_we (request):
    if request.method == 'POST':
        idWE = request.POST['id_we']
        elemWE = WE.objects.all()[int(idWE) - 1]
        elemWE.company = request.POST['company_edit_we']
        elemWE.job = request.POST['job_edit_we']
        elemWE.description = request.POST['description_edit_we']
        elemWE.save()
        print(request.POST)
    return redirect('/')
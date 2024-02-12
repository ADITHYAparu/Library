from django.shortcuts import render,redirect,HttpResponse
from app.models import idgen,tbl_member,tbl_login,tbl_book,tbl_review,tbl_request,tbl_issue,tbl_return
from django.core.files.storage import FileSystemStorage
import datetime
from django.core.mail import send_mail
def page1(request):
    return render(request,"program.html")
def login(request):
    return render(request,"logins.html")
def page3(request):
    return render(request,"reg.html")
def membership(request):
    return render(request,"membership.html")  
def membership1(request):
    data=idgen.objects.get(id=1)
    f=data.mid
    f=f+1
    f1="MEMBER"+str(f)
    data = tbl_member()
    data.memberid=f1
    data.name=request.POST.get('name')
    data.address=request.POST.get('address')
    data.phone=request.POST.get('phone')
    data.email=request.POST.get('email') 
    data.status="notverified"
    data.save() 
    data1=idgen.objects.get(id=1)
    data1.mid=f
    data1.save()
    
    return render(request,"membership.html",{'d1':1})
def login1(request):
    data=tbl_login.objects.all()
    if request.method == 'POST':
        
        username=request.POST.get('username')  
        password=request.POST.get('password')
        flag=0
        for da in data:
            if username==da.username and password==da.password:
                type=da.category
                flag=1
                
                if type=="admin":
                    request.session['uid']=username
                    return redirect('/adminhome')
                elif type=="member":
                    request.session['member']=username
                    return redirect('/memberhome')
                
                else:
                    return render(request,"log.html", {'error': "Invalid"})  
                    #return HttpResponse("Invalid")
        if flag==0:
            #return HttpResponse("user doesn't exist")  
            return render(request,"log.html", {'error': "Invalid username or password"}) 
def adminlogout(request):
     del request.session['uid']
     return render(request,"program.html")    
def adminhome(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        return render(request,"adminhome.html") 
def addbook(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        return render(request,"addbook.html")   
def addbook1(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        c=tbl_book.objects.filter(name=request.POST.get('name')).filter(volume=request.POST.get('volume')).count()
        if c==0:
            data=idgen.objects.get(id=1)
            f=data.bid
            f=f+1
            f1="BOOK"+str(f)
            data = tbl_book()
            data.bookid=f1
            data.name=request.POST.get('name')
            data.category=request.POST.get('category')
            data.volume=request.POST.get('volume')
            data.author=request.POST.get('author') 
            data.publisher=request.POST.get('publisher') 
            data.publishingdate=request.POST.get('publishingdate') 
            data.availablenumber=request.POST.get('availablenumber') 
            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.photo=uploaded_file_url
            data.status="available"
            data.save() 
            data1=idgen.objects.get(id=1)
            data1.bid=f
            data1.save()
        
            return render(request,"addbook.html",{'d1':1})    
        else:
            return HttpResponse("Already Exist...........")               
def removebook(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_book.objects.all()
        return render(request,"removebook.html",{'data':data})    
def removebook1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_book.objects.get(bookid=id)
        data.delete()
   
        return redirect('/removebook')    
def verifymember(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_member.objects.filter(status="notverified")
        return render(request,"verifymember.html",{'data':data})    
def acceptmember(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_member.objects.get(memberid=id)
        data.status="verified"
        data.save()
        data2=tbl_login()
        data2.username=data.memberid
        data2.password=data.phone
        data2.category="member"


        data2.save()
   
        return redirect('/verifymember') 
def memberlogout(request):
     del request.session['member']
     return render(request,"program.html")   
def memberhome(request):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        return render(request,"memberhome.html")   
def searchbook(request):
        data=tbl_book.objects.all()
        return render(request,"searchbook.html",{'data':data})  
def givereview(request,id):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        return render(request,"givereview.html",{'id':id})      
def givereview1(request,id2):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        data=idgen.objects.get(id=1)
        f=data.rid
        f=f+1
        f1="REVIEW"+str(f)
        data = tbl_review()
        data.reviewid=f1
        data.bookid_id=id2
        data.memberid_id=request.session['member']
        data.review=request.POST.get('review')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.date= time1
        data.save() 
        data1=idgen.objects.get(id=1)
        data1.rid=f
        data1.save()
    
        return redirect('/searchbook')          
def viewreview(request,id):
        data=tbl_review.objects.filter(bookid_id=id)
        return render(request,"viewreview.html",{'data':data})  
def searchbook1(request):
        data=tbl_book.objects.all()
        return render(request,"searchbook1.html",{'data':data})     
def viewreview1(request,id):
        data=tbl_review.objects.filter(bookid_id=id)
        return render(request,"viewreview1.html",{'data':data})       
def requestbook(request,id2):
        d3=tbl_book.objects.get(bookid=id2)
        d2=tbl_member.objects.get(memberid=request.session['member'])
        return render(request,"requestbook.html",{'id':id2,'d3':d3,'d2':d2})      
def requestbook1(request,id2):
        data=idgen.objects.get(id=1)
        f=data.rdid
        f=f+1
        f1="REQUEST"+str(f)
        data = tbl_request()
        data.requestid=f1
        data.bookid_id=id2
        data.memberid_id=request.session['member']
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.date= time1
        data.status="pending"
        data.save() 
        data1=idgen.objects.get(id=1)
        data1.rdid=f
        data1.save()
    
        return redirect('/searchbook')      
def viewrequest(request):
        data=tbl_request.objects.filter(status="pending")
        return render(request,"viewrequest.html",{'data':data})    
def acceptrequest(request,id):
        return render(request,"acceptrequest.html",{'id':id}) 
def requeststatus(request):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_request.objects.filter(memberid_id=request.session['member']).filter(status="accepted")
        return render(request,"requeststatus.html",{'data':data})     
def requeststatus1(request,id):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_issue.objects.get(requestid_id=id)
        return render(request,"requeststatus1.html",{'data':data})         
def returnbook(request):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_issue.objects.filter(memberid_id=request.session['member']).filter(status="pending")
        return render(request,"returnbook.html",{'data':data})  
def returnbook1(request,id):
    if 'member' not in request.session:
        return render(request,"logins.html")
    else:
        data=idgen.objects.get(id=1)
        f=data.rtid
        f=f+1
        f1="RETURN"+str(f)
        data = tbl_return()
        data.returnid=f1
        data.issueid_id=id
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.date= time1
        data.status="pending"
        data.save()
        data1=idgen.objects.get(id=1)
        data1.rtid=f
        data1.save()
        dat=tbl_issue.objects.get(issueid=id)
        dat.status="member returned"
        dat.save()
        return render(request,"memberhome.html")    
def acceptrequest1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data3=tbl_request.objects.get(requestid=id)
        data=idgen.objects.get(id=1)
        f=data.isid
        f=f+1
        f1="ISSUE"+str(f)
        data = tbl_issue()
        data.issueid=f1
        data.requestid_id=id
        data.memberid_id=data3.memberid_id
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.date= time1
        data.status="pending"
        data.expecteddate=request.POST.get('expecteddate')
        data.save() 
        data1=idgen.objects.get(id=1)
        data1.isid=f
        data1.save()
        data3=tbl_request.objects.get(requestid=id)
        data3.status="accepted"
        data3.save()
        d=tbl_member.objects.get(memberid=data3.memberid_id)
        send_mail('message','expected date'+data.expecteddate,'from@example.co',[d.email,])

    
        return redirect('/viewrequest')      
def searchbookpublic(request):
    return render(request,"searchbookpublic.html")
def searchbookpublic1(request):
    data=request.POST.get('name')
    if data:
        result=tbl_book.objects.filter(name__icontains=data)
        return render(request,"searchbookpublic.html",{'data':result})


def searchbookmember(request):
    return render(request,"searchbookpublic.html")
def searchbookmember1(request):
    data=request.POST.get('name')
    if data:
        result=tbl_book.objects.filter(name__icontains=data)
        return render(request,"searchbookpublic.html",{'data':result})
def viewreturn(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_return.objects.filter(status="pending")
        return render(request,"viewreturn.html",{'data':data})      
def viewreturn1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data=tbl_return.objects.get(returnid=id)
        data.status="approved"
        data.save()
        data1=tbl_issue.objects.get(issueid=data.issueid_id)
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data1.returndate=time1
        data1.save()
        return render(request,"adminhome.html")          
def book(request):
    data=tbl_book.objects.all()
    return render(request,"book.html",{'data':data})       
def member(request):
    data=tbl_member.objects.all()
    return render(request,"member.html",{'data':data})    
          



# Create your views here.

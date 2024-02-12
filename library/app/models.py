from django.db import models
class tbl_member(models.Model):
    memberid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table ="tbl_member"
class tbl_login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=90)
    category = models.CharField(max_length=90)
    class Meta:
        db_table ="tbl_login"        
class idgen(models.Model):
    mid = models.IntegerField()
    bid = models.IntegerField()
    rid = models.IntegerField()
    rdid = models.IntegerField()
    isid = models.IntegerField()
    rtid=models.IntegerField()
 
    class Meta:
        db_table ="idgen"   
class tbl_book(models.Model):
    bookid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=90)
    category= models.CharField(max_length=90)
    volume = models.CharField(max_length=90)
    author = models.CharField(max_length=90)
    publisher = models.CharField(max_length=90)
    publishingdate = models.CharField(max_length=90)
    availablenumber = models.CharField(max_length=90)
    photo = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table ="tbl_book"  
class tbl_review(models.Model):
    reviewid = models.CharField(primary_key=True, max_length=50)
    bookid =models.ForeignKey(tbl_book, on_delete=models.CASCADE)
    memberid =models.ForeignKey(tbl_member, on_delete=models.CASCADE)
    review= models.CharField(max_length=150)
    date = models.CharField(max_length=90)

    class Meta:
        db_table ="tbl_review"   
class tbl_request(models.Model):
    requestid = models.CharField(primary_key=True, max_length=50)
    bookid =models.ForeignKey(tbl_book, on_delete=models.CASCADE)
    memberid =models.ForeignKey(tbl_member, on_delete=models.CASCADE)
    status= models.CharField(max_length=90)
    date = models.CharField(max_length=90)

    class Meta:
        db_table ="tbl_request"       
class tbl_issue(models.Model):
    issueid = models.CharField(primary_key=True, max_length=50)
    requestid =models.ForeignKey(tbl_request, on_delete=models.CASCADE)
    memberid =models.ForeignKey(tbl_member, on_delete=models.CASCADE)
    status= models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    expecteddate = models.CharField(max_length=90)
    returndate = models.CharField(max_length=90)

    class Meta:
        db_table ="tbl_issue"            
class tbl_return(models.Model):
    returnid = models.CharField(primary_key=True, max_length=50)
    issueid =models.ForeignKey(tbl_issue, on_delete=models.CASCADE)
    
    status= models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    class Meta:
        db_table ="tbl_return"                                          
# Create your models here.

# Create your models here.

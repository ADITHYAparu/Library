"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('adminlogout/',views.adminlogout),
    path('memberlogout/',views.memberlogout),
    path('admin/', admin.site.urls),
    path('index1/',views.page1),
    path('login/',views.login),
    path('index3/',views.page3),
    path('membership/',views.membership),
    path('membership1/',views.membership1),
    path('login1/',views.login1),
    path('adminhome/',views.adminhome),
    path('addbook/',views.addbook),
    path('addbook1/',views.addbook1),
    path('removebook/',views.removebook),
    path('removebook1/<str:id>',views.removebook1),
    path('verifymember/',views.verifymember),
    path('acceptmember/<str:id>',views.acceptmember),
    path('memberhome/',views.memberhome),
    path('searchbook/',views.searchbook),
    path('givereview/<str:id>',views.givereview),
    path('viewreview/<str:id>',views.viewreview),
    path('givereview1/<str:id2>',views.givereview1),
    path('searchbook1/',views.searchbook1),
    path('viewreview1/<str:id>',views.viewreview1),
    path('requestbook/<str:id2>',views.requestbook),
    path('requestbook1/<str:id2>',views.requestbook1),
    path('viewrequest/',views.viewrequest),
    path('acceptrequest/<str:id>',views.acceptrequest),
    path('acceptrequest1/<str:id>',views.acceptrequest1),
    path('requeststatus/',views.requeststatus),
    path('requeststatus1/<str:id>',views.requeststatus1),
    path('returnbook/',views.returnbook),
    path('returnbook1/<str:id>',views.returnbook1),
    path('searchbookpublic/',views.searchbookpublic),
    path('searchbookpublic1/',views.searchbookpublic1),
    path('searchbookmember/',views.searchbookmember),
    path('searchbookmember1/',views.searchbookmember1),
    path('viewreturn/',views.viewreturn),
    path('viewreturn1/<str:id>',views.viewreturn1),
    path('book/',views.book),
    path('member/',views.member),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




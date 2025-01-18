"""
URL configuration for RealEstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from estate import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estate/add/',views.PropertyCreateView.as_view(),name='addrealestate'),
    path('estate/list/',views.RealEstateListView.as_view(),name='listrealestate'),
    path('estste/<int:pk>/',views.RealEstateDetailView.as_view(),name='detailestate'),
    path('estate/<int:pk>/remove',views.RealEstateDeleteView.as_view(),name='deleteestate'),
    path('estate/<int:pk>/changes/',views.RealEstateUpdateView.as_view(),name='updateestate'),
    path('estate/summary/',views.RealEstateSummaryView.as_view(),name="summaryestate"),
    path('register/',views.SignUpView.as_view(),name='signup'),
    path('',views.SignInView.as_view(),name='signin'),
    path('signout/',views.SignOutView.as_view(),name='signout'),
    path('estate/home/',views.PropertyHomeView.as_view(),name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

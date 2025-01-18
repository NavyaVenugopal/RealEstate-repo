from django.shortcuts import render,redirect

from django.views.generic import View

from estate.forms import RealEstateCreateForm,SignUpForm,LoginForm

from estate.models import PropertyDetails

from django.db.models import Count

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator

from estate.decorators import signin_required

from django.contrib import messages

from django.db.models import Q

# Create your views here.

@method_decorator(signin_required,name='dispatch')
class PropertyHomeView(View):
    
    template_name = "property_home.html"
    
    def get(self,request,*args,**kwargs):
    
        return render(request, self.template_name)
    

@method_decorator(signin_required,name='dispatch')

class PropertyCreateView(View):
    
    template_name = "property_add.html"
    
    form_class = RealEstateCreateForm
    
    def get(self,request,*args,**kwargs):
        
        form = self.form_class   #creating form_instance
        
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = self.form_class(request.POST,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.instance.owner=request.user
            
            form_instance.save()  #creating
            
            # data = form_instance.cleaned_data
            
            # PropertyDetails.objects.create(**data)
            messages.success(request,"Property Successfully Created...")
            
            return redirect('listrealestate')
        
 
@method_decorator(signin_required,name='dispatch')
       
class RealEstateListView(View):
    
    template_name = 'property_list.html'
    
    def get(self,request,*args,**kwargs):
        
        
        selected_category = request.GET.get('category','all')
        
        search_text = request.GET.get("search-text")
        
        if search_text:
            
            qs = PropertyDetails.objects.filter(owner=request.user)
            
            qs = qs.filter(Q(property_type__contains=search_text)|Q(property_status__contains=search_text))
        
        elif selected_category == 'all':
            
            qs = PropertyDetails.objects.filter(owner=request.user)
            
        else:
            
            qs = PropertyDetails.objects.filter(property_type=selected_category,owner=request.user)
            
        categories = PropertyDetails.objects.all().values_list("property_type",flat=True).distinct()
            
        print(categories)
        
        search = PropertyDetails.objects.all().values_list(flat=True).distinct()
        
        print(search)
        
        return render(request,self.template_name,{'data':qs,"categories":categories,'selected_category':selected_category})
    
    
@method_decorator(signin_required,name='dispatch')
class RealEstateDetailView(View):
    
    template_name = 'property_details.html'
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get('pk')
        
        qs = PropertyDetails.objects.get(id=id)
        
        return render(request,self.template_name,{"data":qs})
    
    
@method_decorator(signin_required,name='dispatch')
class RealEstateDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get('pk')
        
        PropertyDetails.objects.get(id=id).delete()
        
        messages.error(request,"Property Deleted Successfully")
        
        return redirect('listrealestate')
    
@method_decorator(signin_required,name='dispatch')
class RealEstateUpdateView(View):
    
    template_name = 'property_update.html'
    
    form_class = RealEstateCreateForm
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get('pk')
        
        estate_obj = PropertyDetails.objects.get(id=id)
        
        form_instance = self.form_class(instance=estate_obj)
        
        # instance_dict = {'property_name':instance.property_name,'property_type':instance.property_type,'property_stauts':instance.property_status,'location':instance.location,'address':instance.address,'price':instance.price,'area':instance.area,'no_of_rooms':instance.no_of_rooms,'furnished_status':instance.furnished_status}
        
        # form_instance = self.form_class(initial=instance_dict)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id = kwargs.get('pk')
        
        estate_obj = PropertyDetails.objects.get(id=id)
        
        form_instance = self.form_class(request.POST,request.FILES,instance=estate_obj)
        
        if form_instance.is_valid():
            
            # data = form_instance.cleaned_data
            # PropertyDetails.objects.filter(id=id_data).update(**data)
            
            form_instance.save()
            
            messages.success(request,"Updated successfully")
            
            return redirect('listrealestate')
        
@method_decorator(signin_required,name='dispatch')       
class RealEstateSummaryView(View):
    
    template_name = "property_summary.html"
    
    def get(self,request,*args,**kwargs):
        
        total_registrations = PropertyDetails.objects.filter(owner=request.user).aggregate(total=Count("property_name"))
        
        property_type_summary = PropertyDetails.objects.filter(owner=request.user).values("property_type").annotate(total=Count("property_type"))
        
        property_status = PropertyDetails.objects.filter(owner=request.user).values("property_type",'property_status').annotate(total=Count("property_type"))
        
        print(property_type_summary)
        
        context = {
            'total_registration':total_registrations['total'],
            'property_type_summary':property_type_summary,
            'property_status_summary':property_status
        }
        
        return render(request,self.template_name,context)

       
class SignUpView(View):
    
    template_name = "signup.html"
    
    form_class =     SignUpForm
    
    def get(self,request,*args,**kwargs):
        
        form = self.form_class()
        
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = self.form_class(request.POST)
        
        if form_instance.is_valid():
            
            data = form_instance.cleaned_data
            
            # User.objects.create_user(**data)
            
            form_instance.save()
            
            return redirect('signin') 
        
        return render(request,self.template_name,{"form":form_instance})
    
class SignInView(View):
    
    template_name = "login.html"
    
    form_class = LoginForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance = self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = self.form_class(request.POST)
        
        if form_instance.is_valid():
            
            uname = form_instance.cleaned_data.get("username")
            
            pwd = form_instance.cleaned_data.get("password")
            
            user_object = authenticate(request,username=uname,password=pwd)
            
            if user_object:
                
                login(request,user_object)
                
                messages.success(request,"Logged In Successfully")
                
                return redirect('home')

        return render(request,self.template_name,{"form":form_instance})   
 
@method_decorator(signin_required,name='dispatch')   
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        messages.success(request,"Logout!!!!")
    
        return redirect('signin')             
            
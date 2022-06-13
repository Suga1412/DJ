from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class BaseView(View):
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()


class HomeView(BaseView):
	def get(self,request):
		self.views
		self.views['new_products'] = product.objects.filter(labels = 'new')
		self.views['hot_products'] = product.objects.filter(labels = 'hot')
		self.views['offer_products'] = product.objects.filter(labels = 'offer')
		self.views['sliders'] = Slider.objects.all()
		self.views['ads'] = Ad.objects.all()
		return render(request,'index.html',self.views)

class subCategoryView(BaseView):
	def get(self,request): 
		subcat_id = SubCategory.obejcts.get(slug = slug).id
		self.views['subcar_products'] = Product.objects.filter(subcategory_id = subcat_id)
		return render(request,'subcategory.html',self.views)


class DetailView(BaseView):
	def get(self,request,slug):
		self.views['detail_products'] = Product.objects.filter(slug = slug)
		return render(request,'single.html',self.views)		

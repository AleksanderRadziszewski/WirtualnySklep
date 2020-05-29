from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from WirtualnyOptyk.forms import CreateProfileForm, SearchForm
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from WirtualnyOptyk.forms import Supply_Form
from WirtualnyOptyk.models import Frames, Product, ContactLenses, Accessories, Glasses, Profile, Cart, \
    CartProducts, Supply, Order, User, OrderProduct


class SearchProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        form = SearchForm(request.GET)
        form.is_valid()
        name = form.cleaned_data.get('name')
        if name is not None:
            products = Product.objects.filter(name__icontains=name)
        paginator = Paginator(products, 1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'WirtualnyOptyk/product_list.html', {'form': form,
                                                                    'page_obj': page_obj})


class MainPageView(LoginView):
    template_name = "WirtualnyOptyk/main_page.html"


class LogOutView(LogoutView):
    next_page = "/"


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "WirtualnyOptyk/delete.html"
    permission_required = "WirtualnyOptyk.delete_product"
    permission_denied_message = "Sorry,You don't have permissions"
    success_url = "/product_list/"


class ProductDetailView(DetailView):
    model = Product
    template_name = "WirtualnyOptyk/accessories_detail.html"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'WirtualnyOptyk/add.html'
    success_url = '/product_list/'
    permission_required = 'WirtualnyOptyk.change_product'
    permission_denied_message = " Sorry,You don't have permissions"

    def get_success_url(self):
        return f"/product_detail/{self.object.pk}/"


class MenuView(View):
    def get(self, request):
        return render(request, "WirtualnyOptyk/menu.html")


class ContactView(View):
    def get(self, request):
        return render(request, "WirtualnyOptyk/contact.html")


class SearchAccessoriesListView(View):

    def get(self, request):
        accessories = Accessories.objects.all()
        form = SearchForm(request.GET)
        form.is_valid()
        name = form.cleaned_data.get('name')
        if name is not None:
            accessories = accessories.filter(name__icontains=name)
        paginator = Paginator(accessories, 1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'WirtualnyOptyk/accessories_list.html', {'form': form,
                                                                        'page_obj': page_obj})


class AddAccessoriesView(PermissionRequiredMixin, CreateView):
    permission_required = "WirtualnyOptyk.add_accessories"
    permission_denied_message = " Sorry,You don't have permissions"
    model = Accessories
    fields = "__all__"
    template_name = "WirtualnyOptyk/add.html"
    success_url = "/accessories_list/"


class AccessoriesUpdateView(PermissionRequiredMixin, UpdateView):
    model = Accessories
    fields = "__all__"
    template_name = 'WirtualnyOptyk/add.html'
    permission_required = 'WirtualnyOptyk.change_accessories'
    permission_denied_message = "Sorry,You don't have permissions"

    def get_success_url(self):
        return f"/accessories_detail/{self.object.pk}/"


class AccessoriesDeleteView(PermissionRequiredMixin, DeleteView):
    model = Accessories
    template_name = "WirtualnyOptyk/delete.html"
    permission_required = "WirtualnyOptyk.delete_akcesoria"
    permission_denied_message = "Sorry,You don't have permissions"
    success_url = "/accessories_list/"


class AccessoriesDetailView(DetailView):
    model = Accessories
    template_name = "WirtualnyOptyk/accessories_detail.html"


class ContactLensesDeleteView(PermissionRequiredMixin, DeleteView):
    model = ContactLenses
    template_name = "WirtualnyOptyk/delete.html"
    permission_required = "WirtualnyOptyk.delete_contactlenses"
    permission_denied_message = "Sorry,You don't have permissions"
    success_url = "/contact_lenses_list/"


class ContactLensesAddView(PermissionRequiredMixin, CreateView):
    permission_required = "WirtualnyOptyk.add_contactlenses"
    permission_denied_message = "Sorry,You don't have permissions"
    model = ContactLenses
    fields = "__all__"
    template_name = "WirtualnyOptyk/add.html"
    success_url = "/contact_lenses_list/"


class SearchContactLensesListView(View):

    def get(self, request):
        contactlenses = ContactLenses.objects.all()
        form = SearchForm(request.GET)
        form.is_valid()
        name = form.cleaned_data.get('name')
        if name is not None:
            contactlenses = contactlenses.filter(name__icontains=name)
        paginator = Paginator(contactlenses, 1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'WirtualnyOptyk/contact_lenses_list.html', {'form': form,
                                                                           'page_obj': page_obj})


class ContactLensesDetailView(DetailView):
    model = ContactLenses
    template_name = "WirtualnyOptyk/accessories_detail.html"


class ContactLensesUpdateView(PermissionRequiredMixin, UpdateView):
    model = ContactLenses
    fields = "__all__"
    template_name = 'WirtualnyOptyk/add.html'
    permission_required = 'WirtualnyOptyk.change_contactlenses'
    permission_denied_message = "Sorry,You don't have permissions"

    def get_success_url(self):
        return f"/contact_lenses_detail/{self.object.pk}/"


class FrameUpdateView(PermissionRequiredMixin, UpdateView):
    model = Frames
    fields = "__all__"
    template_name = 'WirtualnyOptyk/add.html'
    permission_required = 'WirtualnyOptyk.change_frames'
    permission_denied_message = "Sorry,You don't have permissions"

    def get_success_url(self):
        return f"/frame_detail/{self.object.pk}/"


class FrameAddView(CreateView):
    model = Frames
    fields = "__all__"
    template_name = "WirtualnyOptyk/add.html"
    success_url = "/frames_list/"
    permission_required = 'WirtualnyOptyk.add_frames'
    permission_denied_message = "Sorry,You don't have permissions"


class SearchFrameListView(View):
    def get(self, request):
        frames = Frames.objects.all()
        form = SearchForm(request.GET)
        form.is_valid()
        name = form.cleaned_data.get('name')
        if name is not None:
            frames=frames.filter(name__icontains=name)
        paginator = Paginator(frames, 1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'WirtualnyOptyk/frames_list.html', {'form': form,
                                                                   'page_obj': page_obj})


class FrameDetailView(DetailView):
    model = Frames
    template_name = "WirtualnyOptyk/accessories_detail.html"


class FrameDeleteView(PermissionRequiredMixin, DeleteView):
    model = Frames
    template_name = "WirtualnyOptyk/delete.html"
    permission_required = "WirtualnyOptyk.delete_frames"
    permission_denied_message = "Sorry,You don't have permissions"
    success_url = "/frames_list/"


class GlassesUpdateView(PermissionRequiredMixin, UpdateView):
    model = Glasses
    fields = "__all__"
    template_name = 'WirtualnyOptyk/add.html'
    permission_required = 'WirtualnyOptyk.change_glasses'
    permission_denied_message = "Sorry,You don't have permissions"

    def get_success_url(self):
        return f"/glasses_detail/{self.object.pk}/"


class GlassesAddView(CreateView):
    model = Glasses
    fields = "__all__"
    template_name = "WirtualnyOptyk/add.html"
    success_url = "/glasses_list/"
    permission_required = 'WirtualnyOptyk.add_glasses'
    permission_denied_message = "Sorry,You don't have permissions"


class GlassesDetailView(DetailView):
    model = Glasses
    template_name = "WirtualnyOptyk/accessories_detail.html"


class GlassesDeleteView(PermissionRequiredMixin, DeleteView):
    model = Glasses
    template_name = "WirtualnyOptyk/delete.html"
    permission_required = "WirtualnyOptyk.delete_glasses"
    permission_denied_message = "Sorry,You don't have permissions"
    success_url = "/glasses_list/"


class CreateProfileView(FormView):
    form_class = CreateProfileForm
    template_name = "WirtualnyOptyk/add.html"
    success_url = "/menu/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        Profile.objects.create(user=user, phone_number=form.cleaned_data["phone_number"], adress=form.cleaned_data["adress"])
        return super().form_valid(form)

class ProfileView(DetailView):
    model = Profile
    template_name = "WirtualnyOptyk/profile.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.request.user.order_set.all()
        return context


class AddProductToCart(View):
    def post(self, request):
        cart, created = Cart.objects.get_or_create(client=request.user)
        product = Product.objects.get(id=request.POST.get("id_product"))
        cart.products.add(product)
        return HttpResponse("")


class CartView(DetailView):
    model = Cart
    fields = "__all__"
    template_name = "WirtualnyOptyk/cart.html"

    def get_object(self, queryset=None):
        self.object, created = self.model.objects.get_or_create(client=self.request.user)
        return self.object


class SearchGlassesListView(View):
    def get(self, request):
        glasses = Glasses.objects.all()
        form = SearchForm(request.GET)
        form.is_valid()
        name = form.cleaned_data.get('name')
        if name is not None:
            glasses = glasses.filter(name__icontains=name)
        paginator = Paginator(glasses, 1)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'WirtualnyOptyk/glass_list.html', {'form': form,
                                                                  'page_obj': page_obj})

class ChangeQuantity(View):
    def post(self, request, product_id):
        cart,created = Cart.objects.get_or_create(client=request.user)
        product = Product.objects.get(pk=product_id)
        kp = CartProducts.objects.get(cart=cart, product=product)
        if request.POST.get('type') == '+':
            kp.quantity += 1
        elif request.POST.get("type") == "-":
            kp.quantity -= 1
        else:
            kp.quantity = 0
        kp.save()
        return redirect(f"/cart_display/{cart.pk}")


class OrderView(View):
    def get(self,request):
        form = Supply_Form()
        return render(request, 'WirtualnyOptyk/order.html', {"form":form})
    def post(self,request):
        cart = request.user.cart
        form=Supply_Form(request.POST)
        if form.is_valid() and cart.products.all().count()>0:
            order = form.save(commit = False)
            order.client=request.user
            order.save()
            for kp in cart.cartproducts_set.all():
                OrderProduct.objects.create(order=order,product=kp.product,quantity=kp.quantity)
            cart.products.clear()
            return redirect(f"/order_detail/{order.id}/")

        return render(request, 'WirtualnyOptyk/order.html', {"form": form})

class OrderDetailView(DetailView):
    model = Order
    template_name = "WirtualnyOptyk/order_detail.html"

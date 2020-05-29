"""WirtualnySklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from WirtualnyOptyk import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path('admin/', admin.site.urls),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path('add_frame/', views.FrameAddView.as_view(), name="add frame"),
    path('delete_frame/<int:pk>/', views.FrameDeleteView.as_view(), name="delete frame"),
    path('frame_detail/<int:pk>/', views.FrameDetailView.as_view(), name="frame detail"),
    path('frames_list/', views.SearchFrameListView.as_view(), name="frames list"),
    path('frame_update/<int:pk>/', views.FrameUpdateView.as_view(), name="frame update"),
    path('add_contact_lenses/', views.ContactLensesAddView.as_view(), name="add contact lenses"),
    path('products_list/', views.SearchProductListView.as_view(), name="products_list"),
    path('contact_lenses_list/', views.SearchContactLensesListView.as_view(), name="contact lenses list"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name="delete product"),
    path('product_update/<int:pk>/', views.ProductUpdateView.as_view(), name="product update"),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name="product detail"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('accessories_list/', views.SearchAccessoriesListView.as_view(), name="accessories_list"),
    path('add_accessories/', views.AddAccessoriesView.as_view(), name="add accessories"),
    path('accessories_detail/<int:pk>/', views.AccessoriesDetailView.as_view(), name="accessories detail"),
    path('accessories_delete/<int:pk>/', views.AccessoriesDeleteView.as_view(), name="accessories delete"),
    path('delete_accessories/<int:pk>/', views.AccessoriesDeleteView.as_view(), name="delete accessories"),
    path('accessories_update/<int:pk>/', views.AccessoriesUpdateView.as_view(), name="accessories update"),
    path('contact_lenses_update/<int:pk>/', views.ContactLensesUpdateView.as_view(), name="contact lenses update"),
    path('delete_contact_lenses/<int:pk>/', views.ContactLensesDeleteView.as_view(), name="contact lenses delete"),
    path('contact_lenses_detail/<int:pk>/', views.ContactLensesDetailView.as_view(), name="contact lenses detail"),
    path('add_glasses/', views.GlassesAddView.as_view(), name="add glasses"),
    path('glasses_delete/<int:pk>/', views.GlassesDeleteView.as_view(), name="glasses_delete"),
    path('glasses_detail/<int:pk>/', views.GlassesDetailView.as_view(), name="glasses detail"),
    path('glasses_list/', views.SearchGlassesListView.as_view(), name="glasses list"),
    path('glasses_update/<int:pk>/', views.GlassesUpdateView.as_view(), name="glasses update"),
    path('create_profile/', views.CreateProfileView.as_view(), name="create profile"),
    path("add_product_to_cart/", views.AddProductToCart.as_view(), name="add product to cart"),
    path("cart_display/<int:pk>/", views.CartView.as_view(), name="cart display"),
    path("change_quantity/<int:product_id>", views.ChangeQuantity.as_view(), name="change quantity"),
    path("order/", views.OrderView.as_view(), name="order"),
    path("order_detail/<int:pk>/", views.OrderDetailView.as_view(), name="order detail"),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

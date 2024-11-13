from django.urls import path
from .views import InvoiceView

urlpatterns = [
    path('api/invoices/', InvoiceView.as_view()),       # For POST request
    path('api/invoices/<int:pk>/', InvoiceView.as_view())  # For PUT request
]

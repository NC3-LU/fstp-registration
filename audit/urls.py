from django.urls import path

from audit import views

urlpatterns = [
    path("", views.index, name="audit"),
    path("signup/", views.signup, name="signup"),
    path("product/<int:audit_id>", views.audit),
    path("edit/<int:audit_id>", views.edit, name="edit"),
    path("company/", views.edit_company, name="create_company"),
    path("company/<int:company_id>/", views.edit_company, name="edit_company"),
]

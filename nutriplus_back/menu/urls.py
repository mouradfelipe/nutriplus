from django.urls import path

from .views import AutoGenerateMenu

urlpatterns = [
    path(r'generate/<int:meal>/<int:patient>/', AutoGenerateMenu.as_view(), name="Teste"),
]
from django.urls import path
from questoes.views import *

urlpatterns = [
    path("", GerarQuestoesView.as_view(), name="gerar-questoes" ),
]

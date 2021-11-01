from django.urls import path
from num2word import views

urlpatterns = [
    path("num2word", views.numword, name="num2word"),
    # path("answer", views.answer, name="answer")
]

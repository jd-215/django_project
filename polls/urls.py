from django.urls import path
# from .views import polls_detail, polls_list
from .apiviews import PollList, PollDetail
from .apiviews import ChoiceList, CreateVote, UserCreate,  LoginView, PollViewSet

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('polls', PollViewSet)

urlpatterns = [

    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote/', CreateVote.as_view(), name="create_vote"),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='created_vote'),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('login/', views.obtain_auth_token, name="login"),
    # path('login/', LoginView.as_view(), name="login"),


]

urlpatterns += router.urls

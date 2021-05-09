from django.conf import settings
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name="club"

urlpatterns = [
    # path('', views.home),
    path('', views.index, name='index'),

    # urls for user login/register/logout
    path('register/', views.RegisterClub, name='register'),
    path('signUp/', views.signup, name='signUp'),
    path('signOut/', views.signOut, name='signOut'),
    path('signIn/', views.signIn, name='signIn'),
    path('createEvent/',views.createEvent,name="createEvent"),
    path('myClubs/',views.myClubs,name="myClubs"),
    path('onGoingEvents/',views.onGoingEvents,name="events"),










    # urls for password reset
    # 1. for entering email to reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='AdventureClubs/password_reset.html'),
         name='password_reset'),

    # 2. for sending email to user who want to change password
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='AdventureClubs/password_reset_sent.html'),
         name='password_reset_done'),
    # 3. The link from email on which user clicks to reset password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='AdventureClubs/password_reset_fill.html'),
         name='password_reset_confirm'),
    # 4. on successful reset of password
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='AdventureClubs/password_reset_complete.html'),
         name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
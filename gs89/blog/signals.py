from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender , request , user ,**kwargs):
    print(".........................")
    print("Logged in singnal ........ run intro..")
    print("sender: ",sender)
    print("request: ",request)
    print("user: ",user)
    print("user password: ",user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out , sender=User)
def log_out(sender,request,user,**kwargs):
    print(".........................")
    print("Logged out singnal ........ run intro..")
    print("sender: ",sender)
    print("request: ",request)
    print("user: ",user)
    print("user password: ",user.password)
    print(f'kwargs: {kwargs}')

# user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed )
def log_failed(sender,credentials,request,**kwargs):
    print(".........................")
    print("Login failed singnal ........ run intro..")
    print("sender: ",sender)
    print("Credentials:",credentials)
    print("request: ",request)
    print(f'kwargs: {kwargs}')

# user_login_failed.connect(login_failed,sender=User)

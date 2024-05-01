from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    verbose_name = '마이앱' # admin 앱에서 레이블을 표시할 때 쓰임

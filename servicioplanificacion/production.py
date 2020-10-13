from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'planificacion',
        'USER' : 'icf',
        'PASSWORD' : 'Secret.123',
        'DEFAULT-CHARACTER-SET' : 'utf8',
        'HOST' : '192.168.0.2',
        'PORT' : '3306',
        'TEST': {
            'NAME': 'planificacion_test',
        }
    },
}

STATIC_ROOT="/servicioplanificacion/static"

DEBUG=False

SECRET_KEY=os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True

INSTALLED_APPS += ('corsheaders',)
MIDDLEWARE += ('corsheaders.middleware.CorsMiddleware',)
CORS_ORIGIN_ALLOW_ALL = True

"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mxll($(0b4_&10c061-*s469tjg#u48jh2oi-n6m1fh6_mf5i#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig' , 
    'homemain.apps.HomeMainConfig' ,
    'user_inform.apps.UserInformConfig' ,
    'board.apps.BoardConfig',
]   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', # engine: mysql
    #     'NAME' : 'sampledb', # DB Name
    #     'USER' : 'admin', # DB User
    #     'PASSWORD' :'password',# Password
    #     'HOST': 'database-1.cbmkaqoy0er5.ap-northeast-1.rds.amazonaws.com', # 생성한 데이터베이스 엔드포인트
    #     'PORT': '3306', # 데이터베이스 포트
    #     'OPTIONS':{
    #         'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # }
    #### RDS 연결
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rookies08grdb',
        'USER': 'admin',
        'PASSWORD': 'rookies08gr!',
        'HOST': 'rookies08grdb.ch8y8cm0cecj.us-west-1.rds.amazonaws.com',
        'PORT': '3306',
    }
    ### 로컬 연걸
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'test_db',
    #     'USER': 'root',
    #     'PASSWORD': 'asdf1234',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
   # 'default': {
     #   'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': BASE_DIR / 'db.sqlite3',
    #}
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	BASE_DIR / 'static', 
]

EDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 로그인 성공후 이동하는 URL
LOGIN_REDIRECT_URL = '/index'
LOGIN_URL = '/accounts/login/'          # 로그인 URL
LOGOUT_REDIRECT_URL = '/index'            # 로그아웃 후 URL
AUTH_USER_MODEL = "accounts.Users"       # 커스텀 인증 모델

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 
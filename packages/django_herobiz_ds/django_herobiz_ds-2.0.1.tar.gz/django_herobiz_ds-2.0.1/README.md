### django-herobiz-ds

#### Introduction 
demiansoft homepage templates

---
#### Requirements

Django >= 5.0.3
libsass>=0.23.0
django-compressor >= 4.4
django-analyticsds >= 0.3.1
django-calendards >= 0.4.0
django-modalds >= 0.1.0
django-utilsds >= 0.4.0

---
#### Install

```
>> pip install django-herobiz-ds
>> python manage.py makemigrations django_calendards django_modalds
>> python manage.py migrate
>> python manage.py createsuperuser
```

settings.py  
  
```  
INSTALLED_APPS = [    
    ...  
	'django_analyticsds',  
	'django_utilsds',  
	'django_calendards',  
	'django_modalds',  
	  
	'compressor',  
	  
	'django_herobiz_ds',
]

...

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '_static/'),
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  
X_FRAME_OPTIONS = 'SAMEORIGIN'  
  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',  
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  
    'compressor.finders.CompressorFinder',  
)
```

urls.py
```
from django.contrib import admin  
from django.urls import path, include  
from django.conf import settings  
from django.conf.urls.static import static  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', include('django_herobiz_ds.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---
#### Composition

프로젝트 내의 \_data 폴더 안에 herobizds.py 파일을 생성하고 다음과 같은 형식으로 작성한다.

---


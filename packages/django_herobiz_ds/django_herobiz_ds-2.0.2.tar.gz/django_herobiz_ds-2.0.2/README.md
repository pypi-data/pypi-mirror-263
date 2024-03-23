### django-herobiz-ds

#### Introduction 
demiansoft homepage templates

---
#### Requirements

Django >= 5.0.3
libsass>=0.23.0
django-analyticsds >= 0.3.1
django-calendards >= 0.4.0
django-modalds >= 0.1.0
django-utilsds >= 0.4.0

---
#### Install

settings.py  
```  
INSTALLED_APPS = [    
    ...  
	'django_analyticsds',  
	'django_utilsds',  
	'django_calendards',  
	'django_modalds',  
	  
	'django_herobiz_ds',
]

...

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '_static/'),
]

MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  
X_FRAME_OPTIONS = 'SAMEORIGIN'  
  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
```

in the shell
```
>> pip install django-herobiz-ds
>> python manage.py makemigrations django_calendards django_modalds
>> python manage.py migrate
>> python manage.py createsuperuser
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

```
context = {}

# 아래 메뉴에서 다이렉트 링크로 쓰이는 주소가 너무길어서 변수로 사용함
link = 'https://www.gsden.co.kr/'

unique = {
    "components": [
        # [모듈명, 사용할지여부, 메뉴표시명, 메뉴사용여부]
        ['why-us', True, 'Why Us', False],
        ['about', True, 'About', True],
        ['clients', True, '', False],
        ['cta', True, 'Kakao', True],
        ['onfocus', True, '', False],
        ['features', True, 'Departments', True],
        ['services', True, 'Services', True],
        ['testimonials', True, 'Testimonials', True],
        ['faq', True, 'FAQ', True],
        ['portfolio', True, 'Cases', True],
        ['team', True, 'Doctors', True],
        ['contact', True, 'Contact', True],
        ['direct_link', link, '비급여안내', True],
    ],

    # hero1 - 단일 svg 방식으로 첫번째 hero의 파일명을 따른다.
    # hero2 - 다중 svg 방식으로 모든 hero의 파일명을 따른다.
    # hero3 - 단일 jpg 배경화면 방식으로 첫번째 hero의 파일명을 따른다.
    # hero4 - 단일 슬로건 방식으로 첫번째 hero의 텍스트만 보여 준다.

    "hero_type": 'hero4',  # ['hero1', 'hero2', 'hero3', 'hero4']
    "color": '-pink',  # ['', '-blue', '-green', '-orange', '-purple', '-red', '-pink']

    "about": {
        "title": "가락삼성치과는 믿을수 있습니다.",
        "subtitle": "부제목으로 이것이 적당합니다.",
        "image_filename": "about.jpg",
        "tab": [
            {
                "title": "인사말",
                "subtitle": "Consequuntur <strong>inventore</strong> voluptates consequatur",
                "check": [
                    {
                        "h4": "",
                        "p": "Laborum omnis voluptates voluptas qui sit aliquam blanditiis"
                    },
                    {
                        "h4": "Incidunt non veritatis illum ea ut nisi",
                        "p": ""
                    },
                    {
                        "h4": "Omnis ab quia nemo dignissimos rem eum q",
                        "p": "Eius alias aut cupiditate. Dolor voluptates animi nditiis"
                    },
                ]
            },
            {
                "title": "진료철학",
                "subtitle": " omnis voluptates voluptas qui sit aliquam blanditiis",
                "check": [
                    {
                        "h4": "Repudiandae rerum velit modi et officia",
                        "p": "Laborum omnis voluptates voluptas qui sit aliquam blanditiis"
                    },
                    {
                        "h4": "",
                        "p": ""
                    },
                    {
                        "h4": "Omnis ab quia nemo dignissimos rem eum q",
                        "p": "Eius alias aut cupiditate. Dolor voluptates animi nditiis"
                    },
                ]
            },
            {
                "title": "진료방향",
                "subtitle": "Repudiandae rerum velit modi et offici",
                "check": [
                    {
                        "h4": "Repudiandae rerum velit modi et officia",
                        "p": "Laborum omnis voluptates voluptas qui sit aliquam blanditiis"
                    },
                    {
                        "h4": "Incidunt non veritatis illum ea ut nisi",
                        "p": "Non quod totam minus repellendus autem sint velit. Rerum debitisblanditiis"
                    },
                    {
                        "h4": "Omnis ab quia nemo dignissimos rem eum q",
                        "p": "Eius alias aut cupiditate. Dolor voluptates animi nditiis"
                    },
                ]
            },
        ],
    },

    "cta": {
        "title": "<em>네이버톡톡</em> 상담",
        "desc": "진료에 대한 문의 사항은 네이버 톡톡을 통해 상담 및 예약 가능합니다.",
        "image_filename": "consult.jpg",
        "btns": [
            {
                "title": "네이버 예약 바로가기",
                "link": "https://booking.naver.com/booking/13/bizes/441781",
                "type": "href"  # 'onclick' or 'href'
            },
            {
                "title": "네이버 예약 바로가기",
                "link": "https://booking.naver.com/booking/13/bizes/441781",
                "type": "href"  # 'onclick' or 'href'
            },
        ],
    },

    "onfocus": {
        "h3": "무엇이든 물어보세요.",
        "desc": "문의 사항은 네이버 톡톡을 통해 답변해 드립니다.<br/>(진료시간 이후의 문의는 다음날 확인하고 바로 답변 드리겠습니다.)",
        "li": [
            "치료 비용은 얼마인가요?",
            "이런 치료가 가능한가요?",
            "예약을 하고 싶은데 일정이 가능한가요?",
        ],
        "btn": {
            "title": "네이버 톡톡 바로가기",
            "link": "https://talk.naver.com/ct/w4h6zg",
            "type": "onclick",  # 'onclick' or 'href'
        },
        "video_link": "",
    },

    # 6개를 채우는 것이 좋다.
    # [ "smc", "cmc", "aaid", "snuh", 'eao', "kaomi", 'kaoms', 'sev', 'pnuh', 'kamprs', "ao", 'kugh', 'amc', 'khmc' ]
    "clients": ["smc", "cmc", "aaid", "snuh", 'eao', "kaomi"],

    "portfolio": {
        'title': "CASES",
        'subtitle': '주목할 만한 치과 케이스 모음',
    },
}

context.update(unique)

```
---


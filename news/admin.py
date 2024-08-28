from django.contrib import admin
from news.models import Admin,Contact,Magazine,News,Photo,Video,Logo

'''
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','mobile','email','password','last_login','profile_img')

admin.site.register(Admin,AdminAdmin)
'''

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','mobile','message','date')

admin.site.register(Contact,ContactAdmin)

class MagazineAdmin(admin.ModelAdmin):
    list_display = ('id','date','image','magazine','status')

admin.site.register(Magazine,MagazineAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','heading','datetime','image','type','status')
    #list_editable = ('title','heading','news','image','datetime','type','status')
    list_display_links = ['heading']

admin.site.register(News,NewsAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','category','title','image','status')

admin.site.register(Photo,PhotoAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','category','title','video_id','datetime','status')

admin.site.register(Video,VideoAdmin)

class LogoAdmin(admin.ModelAdmin):
    list_display = ('id','logo','poster','preloader')

admin.site.register(Logo,LogoAdmin)

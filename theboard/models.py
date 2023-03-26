from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    bio = RichTextField(blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    news_susbscribed = models.BooleanField('Newsletter subscription', default=False)

    def __str__(self):
        # получить название поста
        return f'{self.user}'

    def subscribe(self):
        ''' subscribe to the newsletter '''
        self.news_susbscribed = True
        self.save()

    def unsubscribe(self):
        ''' unsubscribe to the newsletter '''
        self.news_susbscribed = False
        self.save()
    
    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/members/{self.user_id}/profile/'


class Post(models.Model):
    TANKS = 'tanks'
    HEALERS = 'healers'
    DD = 'damage dealers'
    MERCHANTS = 'merchants'
    GUILD_MASTER = 'guild masters'
    QUEST_GIVERS = 'questgivers'
    BLACKSMITH = 'blacksmiths'
    LEATHERWORKERS = 'leatherworkers'
    POTION_MAKERS = 'potions makers'
    SPELL_MASTERS = 'spell masters'    

    CATEGORIES = [
        (TANKS, 'tanks'),
        (HEALERS, 'healers'),
        (DD, 'damage dealers'),
        (MERCHANTS, 'merchants'),
        (GUILD_MASTER, 'guild masters'),
        (QUEST_GIVERS, 'questgivers'),
        (BLACKSMITH, 'blacksmiths'),
        (LEATHERWORKERS, 'leatherworkers'),
        (POTION_MAKERS, 'potions makers'),
        (SPELL_MASTERS, 'spell masters'),        
    ]

    title = models.CharField('Title ', max_length=128)
    header_image = models.FileField(null=True, blank=True, upload_to='images/')   
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    post_date = models.DateTimeField('Publication date ', auto_now_add=True)
    body = RichTextUploadingField('Text', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=TANKS)

    def __str__(self):
        return f'{self.title}  |  {self.author}  |  {self.post_date}  |  {self.category}  |  {self.body[:64]}'

    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))

    def get_categories():
        cat_menu = [
        'tanks',
        'healers',
        'damage dealers',
        'merchants',
        'guild masters',
        'questgivers',
        'blacksmiths',
        'leatherworkers',
        'potions makers',
        'spell masters', 
    ]
        return cat_menu
 

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    body = models.TextField('Comment Text')
    date_added = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.post.title} - {self.author.username} - {self.date_added} - {self.body}'
    
    def approve(self):
        ''' approve response/comment '''
        self.approved_comment = True
        self.save()

    def disapprove(self):
        ''' disapprove response/comment '''
        self.approved_comment = False
        self.save()

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/article/{self.post.id}'


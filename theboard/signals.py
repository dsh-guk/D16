from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from django.contrib.auth.models import User  # for creation UserProfile 

from .models import Comment, UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    ''' Signal to automatically create a UserProfile for new users who register on the platform '''
    if created:
        UserProfile.objects.create(user=instance)


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Comment)
def comment_notify(sender, instance, created, **kwargs): 
    ''' Signal to notify the author of a comment about a change in the status of his comment '''
    if instance.approved_comment:
        subject = f'{instance.author}, your response is APPROVED!!!'
        body = f'Dear {instance.author}, your response from {instance.date_added.strftime("%d-%m-%Y")} for the post "{instance.post.title}" by {instance.post.author} is approved ...'
        email = instance.author.email

    if not instance.approved_comment:
        subject = f'{instance.author}, your response was disapproved...'
        body = f'Dear {instance.author}, your response from {instance.date_added.strftime("%d-%m-%Y")} for the post "{instance.post.title}" by {instance.post.author} was disapproved ...'
        email = instance.author.email

    if created:
        subject = f'Dear {instance.post.author}, a new Response from {instance.author} for your post "{instance.post.title}" ...'
        body = f'Dear {instance.post.author}, you have received a Response to your post "{instance.post.title}" from {instance.author} on {instance.date_added.strftime("%d-%m-%Y %H:%M")} ...'
        email = instance.post.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='_@yandex.ru',
        to=[email]  # это то же, что и recipients_list
    )
    
    # получаем наш html
    html_content = render_to_string(
        'theboard/comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем


@receiver(post_delete, sender=Comment)
def delete_comment_notify(sender, instance, **kwargs): 
    ''' signal to notify the author of a comment about the deletion of his comment '''
    subject = f'{instance.author}, your response was DELETED...'
    body = f'Hello, {instance.author}! Your response from {instance.date_added.strftime("%d-%m-%Y")} for the post "{instance.post.title}" by {instance.post.author} was deleted ...'
    email = instance.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='_@yandex.ru',
        to=[email]  # это то же, что и recipients_list
    )
    
    # получаем наш html
    html_content = render_to_string(
        'theboard/comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем


@receiver(post_save, sender=User)
def profile_notify(sender, instance, created, **kwargs):
    ''' Signal to notify the user about changes of his profile settings '''
    subject = f'Hello, {instance.username}! Profile settings has been changed on MMORPG Board!' 
    body = f'Hello, {instance.username}! Profile settings on MMORPG Board has been changed!' 
    email = instance.email

    print(subject)
    print('--------------- \\ --------------')

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='subscribecategory@yandex.ru',
        to=[email]  # это то же, что и recipients_list
    )
    
    # получаем наш html
    html_content = render_to_string(
        'theboard/profile_email.html',
        {
            'userprofile': instance.userprofile,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем


import os
import secrets
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string,get_template
from .models import User, EmailVerificationToken


@receiver(post_save, sender=User)
def verification_email(sender, instance, created, **kwargs):

    if created:

        now = datetime.now()
        user_token = EmailVerificationToken()
        user_token.user_id = instance.id
        user_token.token = secrets.token_urlsafe(64)
        user_token.created_at = int(now.timestamp())
        user_token.updated_at = int(now.timestamp())
        user_token.save()

        token = user_token.token

        if settings.DEBUG:
            url = f'{settings.DEV_URL}/account/verify-email?token={token}'
        else:
            url = f'{settings.LIVE_URL}/account/verify-email?token={token}'

        msg_html = get_template('account/account_verification.html').render({

            'url':url,
            'instance':instance
        })


        send_mail(
            "LMS New Account Verification",

            "Email from LMS.",

            "LMS Admin <os.environ.get('EMAIL_USER')>",

            [instance.email],

            html_message=msg_html,

            fail_silently=False,
        )
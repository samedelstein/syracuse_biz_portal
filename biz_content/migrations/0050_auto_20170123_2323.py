# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-23 23:23
from __future__ import unicode_literals

import biz_content.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biz_content', '0049_auto_20170123_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpage',
            name='page_content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('email', wagtail.wagtailcore.blocks.EmailBlock(classname='email', help_text='Add an email', label='Email', template='biz_content/content_blocks/email_block.html')), ('phone_number', wagtail.wagtailcore.blocks.StructBlock((('phone_number', biz_content.models.CustomCleanRegexBlock(classname='phone_number', custom_clean=biz_content.models.clean_phone_number, error_messages={'invalid': 'Add a ten digit phone number not starting with 1'}, help_text='Add a 10 digit phone number, including area code', label='Phone Number (10 digits)', regex='^\\D*[2-9]\\D*(\\d\\D*){9}$')), ('ext', wagtail.wagtailcore.blocks.IntegerBlock(classname='ext', help_text='Add optional extension', label='Extension', min_value=1, required=False))), classname='phone_number', label='Phone Number')), ('link', wagtail.wagtailcore.blocks.StructBlock((('link_text', wagtail.wagtailcore.blocks.CharBlock()), ('link_url', wagtail.wagtailcore.blocks.URLBlock())), classname='text', help_text='Add resource link', icon='fa-link', label='Link', template='biz_content/content_blocks/url_block.html')), ('alert_text', wagtail.wagtailcore.blocks.CharBlock(classname='alert_text', help_text='Add Alert Text', icon='fa-exclamation', label='Alert Text', max_length=2000, template='biz_content/content_blocks/alert_text.html')), ('embed_block', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='Copy and paste a map or video embed directly here.', icon='fa-code'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='steppage',
            name='page_content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('email', wagtail.wagtailcore.blocks.EmailBlock(classname='email', help_text='Add an email', label='Email', template='biz_content/content_blocks/email_block.html')), ('phone_number', wagtail.wagtailcore.blocks.StructBlock((('phone_number', biz_content.models.CustomCleanRegexBlock(classname='phone_number', custom_clean=biz_content.models.clean_phone_number, error_messages={'invalid': 'Add a ten digit phone number not starting with 1'}, help_text='Add a 10 digit phone number, including area code', label='Phone Number (10 digits)', regex='^\\D*[2-9]\\D*(\\d\\D*){9}$')), ('ext', wagtail.wagtailcore.blocks.IntegerBlock(classname='ext', help_text='Add optional extension', label='Extension', min_value=1, required=False))), classname='phone_number', label='Phone Number')), ('link', wagtail.wagtailcore.blocks.StructBlock((('link_text', wagtail.wagtailcore.blocks.CharBlock()), ('link_url', wagtail.wagtailcore.blocks.URLBlock())), classname='text', help_text='Add resource link', icon='fa-link', label='Link', template='biz_content/content_blocks/url_block.html')), ('alert_text', wagtail.wagtailcore.blocks.CharBlock(classname='alert_text', help_text='Add Alert Text', icon='fa-exclamation', label='Alert Text', max_length=2000, template='biz_content/content_blocks/alert_text.html')), ('embed_block', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='Copy and paste a map or video embed directly here.', icon='fa-code'))), blank=True, null=True),
        ),
    ]

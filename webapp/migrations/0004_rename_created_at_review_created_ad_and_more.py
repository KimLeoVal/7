# Generated by Django 4.0.5 on 2022-08-27 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_product_review_remove_choice_poll_delete_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='created_ad',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='updated_at',
            new_name='updated_ad',
        ),
    ]
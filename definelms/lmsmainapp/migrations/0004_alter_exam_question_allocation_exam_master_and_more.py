# Generated by Django 4.1.1 on 2022-10-15 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmsmainapp', '0003_alter_exam_question_allocation_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_question_allocation',
            name='exam_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid', to='lmsmainapp.exam_master'),
        ),
        migrations.AlterField(
            model_name='exam_question_allocation',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsmainapp.question_bank'),
        ),
    ]
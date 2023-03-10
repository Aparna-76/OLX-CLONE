# Generated by Django 4.1.5 on 2023-02-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='owner',
            new_name='seller',
        ),
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='products',
            name='condition',
        ),
        migrations.AddField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos'),
        ),
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('FASHION', 'Fashion'), ('HOME', 'Home'), ('SPORTS', 'Sports'), ('OTHER', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]

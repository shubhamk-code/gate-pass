from django.db import models
import uuid
from datetime import date
import datetime
# Create your models here.


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.department_name


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250)
    age = models.CharField(null=True, blank=True, max_length=50)
    gender_choices = [('male', "Male"), ('female', "Female"),
                      ('other', "Other"), ('notspecified', "Not Specified")]
    gender = models.CharField(
        max_length=20, choices=gender_choices, default="notspecified")
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


# class Pass(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()


class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    # pass_no = models.ForeignKey(
        # Pass, on_delete=models.CASCADE, default=None, null=True, blank=True)
    # pass_no = models.CharField(max_length=25, default = increment_booking_number, primary_key = True)
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(
        max_length=250, blank=True, null=True, unique=True)
    age = models.CharField(null=True, blank=True, max_length=50)
    gender_choices = [('Male', "Male"), ('Female', "Female"),
                      ('Other', "Other"), ('Notspecified', "Not Specified")]
    gender = models.CharField(
        max_length=20, choices=gender_choices, default="Notspecified")
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(
        Department, default=False, on_delete=models.CASCADE, blank=True, null=True)
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, default=None, null=True, blank=True)
    status_choices = [('Active', 'Active'), ('Inactive',
                                             'Inactive'), ('Cancelled', 'Cancelled')]
    status = models.CharField(
        max_length=15, choices=status_choices, default="Inactive", blank=True, null=True)
    item_choices = [('laptop', "laptop"), ('mobile', "mobile"),
                    ('bag', "bag"), ('files', "files")]
    items = models.CharField(
        max_length=10, choices=item_choices, default=False, blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    ban_choices = [('Banned', 'Banned'), ('Unbanned', 'Unbanned')]
    ban = models.CharField(max_length=10, choices=ban_choices,
                           default="Unbanned", blank=True, null=True)
    session_start = models.DateTimeField(auto_now_add=True)
    session_end = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Contractor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=50)
    mediator_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15, null=True, blank=True)
    contractual = models.CharField(max_length=10, null=True, blank=True)
    # department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.company


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=250)
    address = models.CharField('Venue Address', max_length=250)
    zip_code = models.CharField('ZipCode', max_length=10)
    phone = models.CharField('Contact Phone', max_length=25)
    web = models.URLField('Website Address', null=True, blank=True)
    email = models.EmailField('Event Email')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=250)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(Visitor, blank=True)

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS = (
    (0,"Not a Teenager"),
    (1,"A Teenager")
)



class Male(models.Model):
    FirstName = models.CharField(_("First Name"), max_length=100)
    MiddleName = models.CharField(_("Middle Name"), max_length=100, blank=True, null=True)
    LastName = models.CharField(_("Last Name"), max_length=100)
    Profile_Picture = models.ImageField(_("Profile Picture"),upload_to='male_profile_pic/', help_text=".jpg, .png, .jpeg, .gif, .svg supported", blank=True, null=True)
    DateJoined = models.DateTimeField(_("Song created date"), auto_now_add=True)
    about = models.TextField(_("Bio Details"), max_length=1000, default="")
    address = models.TextField(_("Address Details"), max_length=1000, default="")
    teenage_status = models.IntegerField(choices=STATUS, default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)



    class Meta:
        verbose_name = _("Male")
        verbose_name_plural = _("Males")

    def __str__(self):
        return self.FirstName

class Female(models.Model):
    FirstName = models.CharField(_("First Name"), max_length=100)
    MiddleName = models.CharField(_("Middle Name"), max_length=100, blank=True)
    LastName = models.CharField(_("Last Name"), max_length=100)
    Profile_Picture = models.ImageField(_("Profile Picture"),upload_to='female_profile_pic/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    DateJoined = models.DateTimeField(_("User created date"), auto_now_add=True)
    about = models.TextField(_("Bio Details"), max_length=1000, default="")
    address = models.TextField(_("Address Details"), max_length=1000, default="")
    teenage_status = models.IntegerField(choices=STATUS, default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = _("Female")
        verbose_name_plural = _("Females")

    def __str__(self):
        return self.FirstName


class ChildrenMale(models.Model):
    FirstName = models.CharField(_("First Name"), max_length=100)
    MiddleName = models.CharField(_("Middle Name"), max_length=100, blank=True)
    LastName = models.CharField(_("Last Name"), max_length=100)
    Profile_Picture = models.ImageField(_("Profile Picture"),upload_to='male_profile_pic/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    DOB = models.DateTimeField(_("Date of Birth"), auto_now_add=True)
    DateJoined = models.DateTimeField(_("User created date"), auto_now_add=True)
    present_school = models.CharField(_("Name of School"), max_length=100)
    about = models.TextField(_("Bio Details"), max_length=1000, default="")
    address = models.TextField(_("Address Details"), max_length=1000, default="")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_scholarship_beneficiary = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Male Child")
        verbose_name_plural = _("Male Children")

    def __str__(self):
        return self.FirstName


class ChildrenFemale(models.Model):
    FirstName = models.CharField(_("First Name"), max_length=100)
    MiddleName = models.CharField(_("Middle Name"), max_length=100, blank=True)
    LastName = models.CharField(_("Last Name"), max_length=100)
    Profile_Picture = models.ImageField(_("Profile Picture"),upload_to='female_profile_pic/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    DOB = models.DateTimeField(_("Date of Birth"), auto_now_add=True)
    DateJoined = models.DateTimeField(_("User created date"), auto_now_add=True)
    present_school = models.CharField(_("Name of School"), max_length=100)
    about = models.TextField(_("Bio Details"), max_length=1000, default="")
    address = models.TextField(_("Address Details"), max_length=1000, default="")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_scholarship_beneficiary = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Female Child")
        verbose_name_plural = _("Female Children")

    def __str__(self):
        return self.FirstName


class Attendance(models.Model):
  date = models.DateField()
  male = models.CharField(_("Number of males"), max_length=100)
  female = models.CharField(_("Number of females"), max_length=100)
  childrenMale = models.CharField(_("Number of children males"), max_length=100)
  childrenFemale = models.CharField(_("Number of children females"), max_length=100)
  total = models.CharField(_("Total numbers"), max_length=100, default="0")


class Offering(models.Model):
  date = models.DateField()
  main_church_offering = models.CharField(_("Main Church Offering"), max_length=100)
  children_church_offering = models.CharField(_("Children Church Offering"), max_length=100)
  tithe = models.CharField(_("Tithes"), max_length=100)
  total = models.CharField(_("Total numbers"), max_length=100, default="0")

class Midweek(models.Model):
  date = models.DateField()
  main_church_offering = models.CharField(_("Main Church Offering"), max_length=100)
  children_church_offering = models.CharField(_("Children Church Offering"), max_length=100)
  tithe = models.CharField(_("Tithes"), max_length=100)
  total = models.CharField(_("Total numbers"), max_length=100, default="0")




# Create your models here.

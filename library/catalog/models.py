from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):

    Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Name
    
class Author(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    

    class Meta:
        ordering = ['Last_Name','First_Name']

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.Last_Name} {self.First_Name}"
    
class Language(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author',null = True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField('Genre')
    summary = models.CharField(max_length=600)
    isbn = models.CharField('ISBN',max_length=450,unique=True)
    language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True,null=True)
    
    Loan_status = (
        ('m','Maintenance'),
        ('o', 'On Loan'),
        ('a','Avalaible'),
        ('r','Reserved')
    )
    status = models.CharField(max_length=1,choices=Loan_status,null=True,blank=True)

    class Meta:
        ordering =['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
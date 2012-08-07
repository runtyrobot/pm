from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)                # Project Title
    pub_date = models.DateTimeField('Start date')           # Project Added
    deadline = models.DateTimeField('Estimated deadline')   # Deadline Date
    description = models.TextField()                        # Project description
    attachment = models.CharField(max_length=200)           # Filename for design or possible attachment
    manager = models.CharField(max_length=50)               # Name of the Project manager
    def __unicode__(self):
        return self.title


class Idea(models.Model):
    project = models.ForeignKey(Project)                    # Project ID
    pub_date = models.DateTimeField()                       # When is the idea added
    title   = models.CharField(max_length=150)              # Descriptive title for the idea
    comment = models.TextField()                            # What is the idea
    cstatus = models.IntegerField()                         # What is the status of the idea [-1 = declined | 0 = awaiting approval | 1 = approved ]
    author = models.CharField(max_length=50)                # Who submitted the idea
    modstatus = models.CharField(max_length=50)             # Who approved the idea
    def __unicode__(self):
        return self.title
    
class Bug(models.Model):
    project = models.ForeignKey(Project)                    # Project ID
    pub_date = models.DateTimeField()                       # When is the bug reported
    title   = models.CharField(max_length=150)              # Descriptive title for the bug
    comment = models.TextField()                            # Detailed explaination of the bug
    author = models.CharField(max_length=50)                # Who submitted the bug
    bstatus = models.IntegerField()                         # Current status on the bug [-1 = declined | 0 = awaiting fixing | 1 = fixed ]
    modbug = models.CharField(max_length=50)                # Who fixed the bug
    modcomment = models.TextField()                         # Possible comment on the bugfix
    def __unicode__(self):
        return self.title
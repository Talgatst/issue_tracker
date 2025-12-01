from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    types = models.ManyToManyField(Type, related_name='issues', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary


class IssueType(models.Model):
    issue = models.ForeignKey('webapp.Issue', related_name='issue_types', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.Type', related_name='type_issues', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.issue} | {self.type}'
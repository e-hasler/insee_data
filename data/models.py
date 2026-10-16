from django.db import models

# Contains the essential fields and behaviors of the data we are storing

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True) # no duplicate articles
    publication_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class DataTable(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="tables")
    position = models.PositiveIntegerField()  # ordre du tableau dans l'article
    title = models.CharField(max_length=300, blank=True)
    lecture = models.TextField(blank=True)
    champ = models.TextField(blank=True)
    source = models.TextField(blank=True)
    data = models.JSONField()  # ex. {"headers": [...], "rows": [[...], ...]}

    def __str__(self):
        return f"{self.article.title}, {self.position}"

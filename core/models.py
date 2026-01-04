from django.db import models

class Part(models.Model):
    number = models.CharField(max_length=10, help_text="e.g., 'Part III'")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.number}: {self.title}"

class Article(models.Model):
    number = models.CharField(max_length=20, unique=True, help_text="e.g., '21' or '21A'")
    title = models.CharField(max_length=255)
    content = models.TextField()
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    is_key_article = models.BooleanField(default=False, help_text="Highlight this article in quick views")

    def __str__(self):
        return f"Article {self.number}"

class Amendment(models.Model):
    number = models.IntegerField(unique=True)
    date_enacted = models.DateField(null=True, blank=True)
    description = models.TextField()
    # New fields for detailed view
    reason = models.TextField(blank=True, help_text="Why this amendment was enacted")
    impact = models.TextField(blank=True, help_text="Constitutional impact")
    long_description = models.TextField(blank=True, help_text="Full detailed explanation")
    official_link = models.URLField(blank=True, help_text="Link to official Govt/PRS source")
    
    class Meta:
        ordering = ['-number']

    def __str__(self):
        return f"{self.number}th Amendment"

class Judgment(models.Model):
    title = models.CharField(max_length=255, help_text="e.g., 'Kesavananda Bharati v. State of Kerala'")
    year = models.IntegerField()
    outcome = models.TextField()
    significance = models.TextField()
    related_articles = models.ManyToManyField(Article, blank=True)
    # New fields for source linking
    source_link = models.URLField(blank=True, help_text="Link to contemporary newspaper coverage")
    source_name = models.CharField(max_length=255, blank=True, help_text="e.g., 'The Hindu (1973)'")

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title

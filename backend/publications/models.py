from django.db import models
# noinspection PyUnresolvedReferences
from users.models import CustomUser
from constraints import categories as cats
from multiselectfield import MultiSelectField


class Card(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cards")
    card_name = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    properties = models.JSONField()
    price = models.FloatField()
    num_of_views = models.IntegerField(default=0, editable=False)
    rating = models.FloatField(blank=True, null=True, editable=False)
    time_published = models.DateTimeField(auto_now_add=True, editable=False)
    time_updated = models.DateTimeField(auto_now=True, editable=False)
    is_approved = models.BooleanField(default=False, editable=False)
    favourite = models.ManyToManyField(CustomUser, blank=True, related_name="favourites")
    categories = MultiSelectField(choices=cats)


# Комментарий к товару. Зависим от модели Card
class CardComment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="comments", editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=False)
    related_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments", editable=False)
    text = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    time_published = models.DateTimeField(auto_now_add=True, editable=False)
    time_updated = models.DateTimeField(auto_now=True, editable=False)


# Файл, приложенный к товару. Зависим от модели Card
class CardFile(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="files")
    data = models.FileField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


# Изображение, приложенное к товару. Зависимо от модели Card
class CardImage(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="images")
    data = models.ImageField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


# Изображение, приложенное к отзыву о товаре. Зависим от CardComment
class CardCommentImage(models.Model):
    comment = models.ForeignKey(CardComment, on_delete=models.CASCADE, related_name="images")
    data = models.ImageField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

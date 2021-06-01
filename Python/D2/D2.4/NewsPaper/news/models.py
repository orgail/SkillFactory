from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_author = Post.objects.filter(post_author = self.id, post_choise = self.author)
        total_post_rating = 0
        for post in post_author:
            total_post_rating += post.post_rating * 3

        total_author_comment_rating = 0
        for comments in Comment.objects.filter(comment_user = self.author):
            total_author_comment_rating += comments.comment_rating

        total_author_post_rating = 0
        for comments in Comment.objects.filter(comment_post = post_author):
            total_author_post_rating += comments.comment_rating

        self.author_rating = total_post_rating + total_author_comment_rating + total_author_post_rating
        self.save()


    def __str__(self):
        return str(self.author)

class Category(models.Model):
    category_name = models.CharField(max_length = 80, unique = True)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    article = 'AR'
    news = 'NW'

    POST_TYPE = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_choise = models.CharField(max_length = 2, choices = POST_TYPE, default = news)
    date_in = models.DateField(auto_now_add = True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    post_name = models.CharField(max_length = 120)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[:124] + '...'

    def __str__(self):
        return self.post_name + ', Автор: ' + self.post_author.author.username

class PostCategory(models.Model):
   PC_post = models.ForeignKey(Post, on_delete=models.CASCADE)
   PC_category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date_in = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return 'Пост: ' + self.comment_post.post_name + ', Пользователь: ' + self.comment_user.username
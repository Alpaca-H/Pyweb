from django.db import models


# Create your models here.
class Comment(models.Model):
    People_id = models.CharField(max_length=20, default=False, verbose_name="评论ID")
    advice = models.TextField(default=False, verbose_name='评论建议')
    mail = models.EmailField(default=False, verbose_name='邮箱')
    link = models.CharField(max_length=50, default=False, verbose_name='友链')
    time = models.DateTimeField(verbose_name="评论时间", default=None)

    def __str__(self):
        return self.People_id


class Blog(models.Model):
    title = models.CharField(max_length=20, default=None, verbose_name="博客标题")
    times = models.DateTimeField(verbose_name="时间", default=None)
    author = models.CharField(max_length=20, verbose_name="发布者")
    comments = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    reads = models.PositiveIntegerField(default=0, verbose_name='阅读数')
    text = models.TextField(verbose_name="发表内容")

    class Meta():
        verbose_name = "博客"
        verbose_name_plural = verbose_name
        ordering = ['-times']

    def __str__(self):
        return self.title

    def views_insert(self):
        self.reads = self.reads + 1
        self.save(update_fields=['reads'])

    def views_comment_insert(self):
        self.comments += 1
        self.save(update_fields=["comments"])


class Per_Read(models.Model):
    per_texts = models.TextField()
    times = models.DateTimeField(default=0, verbose_name="时间")
    likes = models.PositiveSmallIntegerField(default=0, verbose_name="喜欢")

    class Meta():
        verbose_name = "每日一句"
        verbose_name_plural = verbose_name
        ordering = ['-times']

    def __str__(self):
        return self.per_texts

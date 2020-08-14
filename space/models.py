from django.db import models

# 사용자 DB  
class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

# 게시글 DB
class Posting(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    picture = models.CharField(max_length=500)
    location = models.CharField(max_length=500)

# commet DB
class User_Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000)
    # user_comment_set.all()

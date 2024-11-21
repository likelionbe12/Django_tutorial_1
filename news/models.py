from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class News(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='news')  # 언론사 참조
    content = models.TextField()  # 뉴스 내용
    published_at = models.DateTimeField(auto_now_add=True)  # 뉴스 등록일 (자동으로 생성된 시간)

    def __str__(self):
        return f"News by {self.company.name} on {self.content}"
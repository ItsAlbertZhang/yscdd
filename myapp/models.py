from django.db import models

# Create your models here.


class TrainClass(models.Model):
    train_classname = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) + ':' + self.train_classname

    class Meta:
        db_table = 'train_class'


class Train(models.Model):
    train_uid = models.IntegerField()
    train_class = models.IntegerField()
    train_capacity = models.IntegerField()
    train_time = models.DateTimeField()

    def __str__(self):
        return str(self.train_uid) + ':' + str(self.train_class) + '=' + str(self.train_capacity) + ' ' + str(self.train_time)

    class Meta:
        db_table = 'train_log'

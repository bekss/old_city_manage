from django.db import models


class Sultan(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Султан'
        verbose_name_plural = 'Султаны'

    def __str__(self):
        return self.name


class Rab(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Раб'
        verbose_name_plural = 'Рабы'

    def __str__(self):
        return self.name


class Soldat(models.Model):
    rab = models.ForeignKey(Rab, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)


    class Meta:
        verbose_name = 'Солдат'
        verbose_name_plural = 'Солдаты'

    def __str__(self):
        return self.name


class Rysar(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    soldat = models.ForeignKey(Soldat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рыцарь'
        verbose_name_plural = 'Рыцари'

    def __str__(self):
        return self.name


class Vazir(models.Model):
    Sultan = models.OneToOneField(Sultan, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50 )
    age = models.CharField(max_length=3)
    status = models.CharField(max_length=15)
    many = models.CharField(max_length=3)
    rysar = models.ForeignKey(Rysar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вазир'
        verbose_name_plural = 'Вазиры'

    def __str__(self):
        return self.name



#Для дальнейшей работы
    # class Status(models.Model):
    #     name_status = models.CharField(max_length=2)
    #
    #     class Meta:
    #         verbose_name = 'Статус'
    #         verbose_name_plural = 'Статусы'
    #
    #     def __str__(self):
    #         return self.name_status
    #
    #
    # class Many(models.Model):
    #     status_many = models.OneToOneField(Status, unique=False, on_delete=models.CASCADE)
    #     many_month = models.CharField(max_length=5)
    #
    #     class Meta:
    #         verbose_name = 'Деньги'
    #         verbose_name_plural = 'Деньги'
    #
    #     def __str__(self):
    #         return self.many_month
    #
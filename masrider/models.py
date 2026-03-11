from django.db import models


class MasRider(models.Model):
    SERIES_CHOICES = [
        ('showa', 'โชวะ (Showa)'),
        ('heisei', 'เฮเซ (Heisei)'),
        ('reiwa', 'เรวะ (Reiwa)'),
    ]

    name = models.CharField(max_length=100, verbose_name="ชื่อ")
    alias = models.CharField(max_length=100, verbose_name="ชื่อมาสไรเดอร์", blank=True)
    age = models.PositiveIntegerField(verbose_name="อายุ", null=True, blank=True)
    series = models.CharField(max_length=10, choices=SERIES_CHOICES, verbose_name="ยุค")
    organization = models.CharField(max_length=200, verbose_name="องค์กร", blank=True)
    transformation_device = models.CharField(max_length=200, verbose_name="อุปกรณ์แปลงร่าง", blank=True)
    abilities = models.TextField(verbose_name="ความสามารถ", blank=True)
    bio = models.TextField(verbose_name="ประวัติ", blank=True)
    image_url = models.URLField(verbose_name="URL รูปภาพ", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "มาสไรเดอร์"
        verbose_name_plural = "มาสไรเดอร์"
        ordering = ['name']

    def __str__(self):
        return f"{self.alias or self.name}"


class CompetitionHistory(models.Model):
    RESULT_CHOICES = [
        ('win', 'ชนะ'),
        ('lose', 'แพ้'),
        ('draw', 'เสมอ'),
    ]

    rider = models.ForeignKey(MasRider, on_delete=models.CASCADE, related_name='competitions', verbose_name="มาสไรเดอร์")
    opponent = models.CharField(max_length=200, verbose_name="คู่ต่อสู้")
    event_name = models.CharField(max_length=200, verbose_name="ชื่อเหตุการณ์")
    event_date = models.DateField(verbose_name="วันที่")
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, verbose_name="ผลการต่อสู้")
    description = models.TextField(verbose_name="รายละเอียด", blank=True)

    class Meta:
        verbose_name = "ประวัติการต่อสู้"
        verbose_name_plural = "ประวัติการต่อสู้"
        ordering = ['-event_date']

    def __str__(self):
        return f"{self.rider} vs {self.opponent} ({self.event_date})"


class Ability(models.Model):
    rider = models.ForeignKey(MasRider, on_delete=models.CASCADE, related_name='special_abilities', verbose_name="มาสไรเดอร์")
    name = models.CharField(max_length=200, verbose_name="ชื่อความสามารถ")
    description = models.TextField(verbose_name="คำอธิบาย", blank=True)
    power_level = models.PositiveIntegerField(verbose_name="ระดับพลัง (1-100)", default=50)

    class Meta:
        verbose_name = "ความสามารถพิเศษ"
        verbose_name_plural = "ความสามารถพิเศษ"

    def __str__(self):
        return f"{self.name} ({self.rider})"

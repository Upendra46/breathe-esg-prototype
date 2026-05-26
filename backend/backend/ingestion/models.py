from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_CHOICES = [
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class IngestionRun(models.Model):

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class RawRecord(models.Model):

    ingestion_run = models.ForeignKey(
        IngestionRun,
        on_delete=models.CASCADE
    )

    raw_json = models.JSONField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class NormalizedActivity(models.Model):

    ACTIVITY_CHOICES = [

        ("fuel","fuel"),
        ("electricity","electricity"),
        ("flight","flight"),
        ("hotel","hotel"),
        ("procurement","procurement"),
    ]

    activity_type=models.CharField(
        max_length=30,
        choices=ACTIVITY_CHOICES
    )

    quantity=models.FloatField()

    unit=models.CharField(
        max_length=20
    )

    scope=models.CharField(
        max_length=20
    )

    status=models.CharField(
        max_length=20,
        default="PENDING"
    )

    source_record=models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )
import uuid

from django.db import models
from django.core.validators import MinValueValidator
from django_tenants.models import TenantMixin, DomainMixin

class Organization(TenantMixin):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    display_name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Optional human-friendly label; falls back to name if empty.",
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        help_text="Stable identifier for subdomains, URLs, and third-party integrations.",
    )
    main_contact_email = models.EmailField()
    main_timezone = models.CharField(max_length=50, default='UTC')

    billing_customer_id = models.CharField(max_length=100, blank=True, null=True)
    plan = models.CharField(max_length=50)
    seats = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=False)
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Store lightweight feature flags or usage limits per tenant.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auto_create_schema = True

class Domain(DomainMixin):
    pass
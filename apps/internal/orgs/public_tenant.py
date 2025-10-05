from models import Organization, Domain

tenant = Organization(
    name="Welcomer Public Tenant",
    display_name="Welcomer Public Tenant",
    on_trial=False,
)

tenant.save()

domain = Domain()
domain.domain = "localhost"
domain.tenant = tenant
domain.is_primary = True
domain.save()
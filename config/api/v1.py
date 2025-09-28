from ninja import NinjaAPI
from scalar_django_ninja import ScalarViewer

from apps.internal.orgs.api_v1 import router as orgs_router

api_v1 = NinjaAPI(
    docs=ScalarViewer(
        openapi_url="/api/v1/openapi.json"
    ),
    docs_url="/docs",
)

api_v1.add_router("/orgs/", orgs_router, tags=["Organizations"])
#api_v1.add_router("/users/", include("apps.api.users.urls"))
#api_v1.add_router("/tenants/", include("apps.api.tenants.urls"))
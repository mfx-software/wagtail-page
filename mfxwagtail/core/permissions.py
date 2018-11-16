from wagtail.core.models import Collection
from core.models import Site
from wagtail.core.permission_policies import ModelPermissionPolicy

site_permission_policy = ModelPermissionPolicy(Site)
collection_permission_policy = ModelPermissionPolicy(Collection)

from django.db.models import QuerySet, Q, Manager


class TenantQuerySet(QuerySet):
    def for_tenant(self, tenant) -> QuerySet:
        return self.filter(tenant=tenant)

    def for_tenant_and_global(self, tenant) -> QuerySet:
        return self.filter(Q(tenant=tenant) | Q(is_global=True))


class TenantManager(Manager):
    def get_queryset(self) -> TenantQuerySet:
        return TenantQuerySet(self.model, using=self._db)

    def for_tenant(self, tenant, include_global=False) -> QuerySet:
        if include_global:
            return self.get_queryset().for_tenant_and_global(tenant)
        return self.get_queryset().for_tenant(tenant)

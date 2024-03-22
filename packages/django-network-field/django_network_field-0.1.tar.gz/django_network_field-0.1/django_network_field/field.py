from django.db import models
from django.db.models import Lookup


class NetworkInclude(Lookup):
    lookup_name = "include"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + lhs_params + rhs_params + lhs_params + rhs_params
        sql = (
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) <= INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) and "
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) + POW(2, 32 - SUBSTRING_INDEX(%s, '/', -1)) - 1 >= "
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) + POW(2, 32 - SUBSTRING_INDEX(%s, '/', -1)) - 1"
        ) % (lhs, rhs, lhs, lhs, rhs, rhs)
        return sql, params


class NetworkCross(Lookup):
    lookup_name = "cross"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = (lhs_params + rhs_params + lhs_params + rhs_params + lhs_params + rhs_params + lhs_params +
                  rhs_params + lhs_params + rhs_params + lhs_params + rhs_params)
        sql = (
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1))  BETWEEN"
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) AND"
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) + POW(2, 32 - SUBSTRING_INDEX(%s, '/', -1)) - 1 OR"
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) + POW(2, 32 - SUBSTRING_INDEX(%s, '/', -1)) - 1 BETWEEN"
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) AND"
            "INET_ATON(SUBSTRING_INDEX(%s, '/', 1)) + POW(2, 32 - SUBSTRING_INDEX(%s, '/', -1)) - 1"
        ) % (lhs, rhs, rhs, rhs, lhs, lhs, rhs, rhs, rhs)
        return sql, params


class NetworkField(models.CharField):
    def get_lookup(self, lookup_name):
        lookup_name_cls = {
            'include': NetworkInclude,
            'cross': NetworkCross,
        }
        return lookup_name_cls.get(lookup_name, super().get_lookup(lookup_name))


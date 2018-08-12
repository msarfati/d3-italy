from . import ma


class RegionSchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'name_en',
            'name_it',
        )


class RegionNameSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
        )


class CitySchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'name_en',
            'name_it',
            'capital',
            'region_id',
        )


class CityNameSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
        )

from . import ma


class RegionSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
        )


class CitySchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
            'capital',
            'region_id',
        )

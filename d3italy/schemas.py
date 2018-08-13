from . import ma


class RegionSchema(ma.Schema):
    capital = ma.Nested('CitySchema')
    class Meta:
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
            'status',
            'population',
            'area',
            'comuni',
            'capital_id',
        )


class CitySchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
            'population',
            'region_id',
        )

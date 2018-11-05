from . import ma


class RegionSchema(ma.Schema):
    capital = ma.Nested('CitySchema', exclude=('region',))
    class Meta:
        strict = True
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
            'status',
            'population',
            'area',
            'comuni',
            'capital',
        )


class CitySchema(ma.Schema):
    region = ma.Nested('RegionSchema', exclude=('city', 'capital'))
    class Meta:
        strict = True
        fields = (
            'id',
            'name',
            'name_en',
            'name_it',
            'population',
            'region',
        )

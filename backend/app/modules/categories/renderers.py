from app.core.renderers import JSONRenderer


class CategoriesJSONRenderer(JSONRenderer):
    object_label = 'categori'
    pagination_object_label = 'categories'
    pagination_count_label = 'categoriesCount'

class ValorationJSONRenderer(JSONRenderer):
    object_label = 'valoration'
    pagination_object_label = 'valorations'
    pagination_count_label = 'valorationsCount'

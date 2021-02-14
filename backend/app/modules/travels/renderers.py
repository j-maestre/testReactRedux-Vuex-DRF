from app.core.renderers import JSONRenderer

class ValorationJSONRenderer(JSONRenderer):
    object_label = 'valoration'
    pagination_object_label = 'valorations'
    pagination_count_label = 'valorationsCount'


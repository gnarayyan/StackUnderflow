from . import models, serializers

NEWS_HELPER_MODELS = ('language',
                      'region',
                      'category',
                      'section')

MODEL = {'language': models.LanguageModel,
         'region': models.RegionModel,
         'category': models.CategoryModel,
         'section': models.SectionModel}
SERIALIZER = {'language': serializers.LanguageSerializer,
              'region': serializers.RegionSerializer,
              'category': serializers.CategorySerializer,
              'section': serializers.SectionSerializer}

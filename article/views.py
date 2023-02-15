from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from article_schema import schema

@csrf_exempt
def graphql_view(request):
    return GraphQLView.as_view(schema=schema)(request)
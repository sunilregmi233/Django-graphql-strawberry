from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from .article_schema import schema
from django.contrib.auth.decorators import login_required

@login_required
def graphql_view(request):
    return GraphQLView.as_view(schema=schema)(request)
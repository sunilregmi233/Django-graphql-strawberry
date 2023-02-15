import strawberry
import typing
from typing import List
from article.models import Article, Author, Tag
from users.models import CustomUser as User


from strawberry.permission import BasePermission
from strawberry.types import Info



class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:

        return False
    
@strawberry.type
class AuthorType:
    id: strawberry.ID
    user: strawberry.ID
    bio: str = strawberry.field(permission_classes=[IsAuthenticated])
    picture: str

@strawberry.type
class TagType:
    id: strawberry.ID
    name: str

@strawberry.type
class ArticleType:
    id: strawberry.ID =  strawberry.field(permission_classes=[IsAuthenticated])
    title: str
    slug: str
    content: str
    created_at: str
    updated_at: str
    author: AuthorType
    tags: List[TagType]
    status: str

@strawberry.type
class Query:
    @strawberry.field
    def articles(self) -> List[ArticleType]:
        return Article.objects.all()

    @strawberry.field
    def article(self, slug: str) -> ArticleType:
        return Article.objects.get(slug=slug)

    @strawberry.field
    def authors(self) -> List[AuthorType]:
        return Author.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_article(self, title: str, slug: str, content: str, author_id: int, tags: List[int], status: str) -> ArticleType:
        author = Author.objects.get(id=author_id)
        article = Article(title=title, slug=slug, content=content, author=author, status=status)
        article.save()
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            article.tags.add(tag)
        return article

    @strawberry.mutation
    def create_author(self, user: int, bio: str, picture: str) -> AuthorType:
        user = User.objects.get(id=user)
        author = Author(user=user, bio=bio, picture=picture)   
        
        author.save()

        return author

schema = strawberry.Schema(query=Query, mutation=Mutation)
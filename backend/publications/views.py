from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import (Card, CardComment, CardFile, CardImage,
                     CardCommentImage)
from .permissions import IsOwnerOrReadOnly, CardFilesImages, CommentFilesImages
from .serializers import (CardSerializer, CardCommentSerializer,
                          CardFileSerializer, CardImageSerializer,
                          CardCommentImageSerializer)
from users.models import CustomUser


class CardViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['time_published', 'time_updated', 'rating', 'owner__rating', 'price']
    filterset_fields = ['time_updated', 'time_published', 'categories', 'rating', 'price', 'owner__rating']
    search_fields = ['card_name', 'caption']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk=None):
        owner, num_of_views = Card.objects.values_list("owner", "num_of_views").get(pk=pk)
        user = CustomUser.objects.values_list("id", flat=True).get(login=request.user)
        print("bb")
        if owner != user:
            print("aa")
            num_of_views += 1
            Card.objects.filter(id=pk).update(num_of_views=num_of_views)
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = CardSerializer(item)
        return Response(serializer.data)


class CardCommentViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        new_rating = 0
        comment_count = 0
        for comment in CardComment.objects.all():
            new_rating += comment.rating
            comment_count += 1

        new_rating /= comment_count + 1
        card = Card.objects.filter(id=self.request.data["card"])
        card.update(rating=new_rating)
        serializer.save(related_user=card.values()[0]["owner_id"])
        CustomUser.objects.filter(id=card.values("owner_id")[0]["owner_id"]).update(rating=new_rating)


class CardImageViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    queryset = CardImage.objects.all()
    serializer_class = CardImageSerializer
    permission_classes = (CardFilesImages,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardFileViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = CardFile.objects.all()
    serializer_class = CardFileSerializer
    permission_classes = (CardFilesImages,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardCommentImageViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              GenericViewSet):
    queryset = CardCommentImage.objects.all()
    serializer_class = CardCommentImageSerializer
    permission_classes = (CommentFilesImages,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

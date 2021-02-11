from django.urls import path
from . import views as publication

urlpatterns = [
    path('api/v1/publication', publication.PublicationListCreateAPIView.as_view()),
    path('api/v1/publication/<int:id>/', publication.PublicationDeletePutGetAPIViewDetail.as_view()),
    path('api/v1/favpub', publication.FavPubsCreateListDestroyAPIView.as_view()),
]
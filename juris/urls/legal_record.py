from django.urls import path, re_path

from juris.views.legal_record import LegalRecordDetailView, LegalRecordListView

urlpatterns = [
    path("", LegalRecordListView.as_view(), name="legal_record_list"),
    path(
        "<slug:code>/",
        LegalRecordDetailView.as_view(),
        name="legal_record_detail",
    ),
]

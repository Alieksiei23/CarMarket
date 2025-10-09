from django.urls import path

from stats.views import BuyerStatsView, SellerStatsView, ShowroomReportView

urlpatterns = [
    path("buyer/", BuyerStatsView.as_view()),
    path("seller/", SellerStatsView.as_view()),
    path('showroom/', ShowroomReportView.as_view()),
]

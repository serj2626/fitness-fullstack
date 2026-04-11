from django.urls import path

from .views import (
    ContactListView,
    FAQListView,
    FeedbackCreateView,
    FooterApiView,
    PolicyApiView,
    SocialListView,
    TermsApiView,
    VacancyListView,
)

urlpatterns = [
    path("", ContactListView.as_view(), name="contact"),
    path("socials/", SocialListView.as_view(), name="social"),
    path("faq-list/", FAQListView.as_view(), name="faq"),
    path("vacancies/", VacancyListView.as_view(), name="vacancy"),
    path("footer/", FooterApiView.as_view(), name="footer"),
    path("feedback/", FeedbackCreateView.as_view(), name="feedback"),
    path("policy/", PolicyApiView.as_view(), name="policy"),
    path("terms/", TermsApiView.as_view(), name="terms"),
]

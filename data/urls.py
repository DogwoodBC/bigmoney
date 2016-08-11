from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from .views import DonationViewSet, ContributorViewSet, ContributorIndividualViewSet, ContributorOrganizationViewSet, \
    FilerViewSet, UniqueIndividualViewSet, UniqueOrganizationViewSet, ElectoralDistrictViewSet

router = routers.DefaultRouter()
router.register(prefix='donations', viewset=DonationViewSet, base_name='donations')
router.register(prefix='contributors', viewset=ContributorViewSet, base_name='contributors')
router.register(prefix='filers', viewset=FilerViewSet, base_name='filers')
router.register(prefix='electoral_districts', viewset=ElectoralDistrictViewSet, base_name='electoral_districts')
# router.register(prefix='unique_individuals', viewset=UniqueIndividualViewSet, base_name='unique_individuals')
# router.register(prefix='unique_organizations', viewset=UniqueOrganizationViewSet, base_name='unique_organizations')

urlpatterns = [
    url(r'^', include(router.urls)),
    # todo Remove test page.
    url(r'^test/$', TemplateView.as_view(template_name='data/test.html')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
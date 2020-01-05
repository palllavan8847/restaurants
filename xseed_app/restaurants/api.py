import json
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf.urls import url

from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.resources import Resource, ModelResource

from models import Restaurant, RestaurantDetail
from views import restaurant_serialize

class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'user'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/api_sorting/$" %(self._meta.resource_name), self.wrap_view('api_sorting'), name="api_sorting"),
            url(r'^(?P<resource_name>%s)/api_logout/$' %(self._meta.resource_name), self.wrap_view('api_logout'), name='api_logout')
        ]
    
    def api_logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        return self.create_response(request, { 'success': False }, HttpUnauthorized)
    
    def api_sorting(self, request, **kwargs):
        data = json.loads(request.body).get('sort')
        res_detail = RestaurantDetail.objects.all()
        for askedOrder in data:
            listOfInstance = res_detail.order_by(askedOrder)
        return self.create_response(request, { 'success': restaurant_serialize(listOfInstance) })
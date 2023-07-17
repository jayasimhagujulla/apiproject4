from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import HttpResponseMixin
import json
# Create your views here.
class studentCRUDCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'no matched record found with matched id'}),status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data)
        qs=student.object.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)




        

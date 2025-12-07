from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Api

class DataApi(APIView):
    def post(self, request):
        data = Api(name=request.data['name'], age=request.data['age'])
        data.save()
        return Response("Sucessfully Saved !!!")

    def get(self,request):
        datas = Api.objects.all()
        data_list = []
        for data in datas:
            data_dict = {
                "id":data.id,
                "name":data.name,
                "age":data.age
            }
            data_list.append(data_dict)
        return Response(data_list)

    def put(self, request, pk):
        data = Api.objects.filter(id=pk)
        data.update(name=request.data['name'], age=request.data['age'])
        return Response('Sucessfully Updated !!!')

    def delete(self, request, pk):
        data = Api.objects.get(id=pk)
        data.delete()
        return Response('Sucessfully Deleted !!!')
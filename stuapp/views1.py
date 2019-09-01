import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stuapp.models import Actor


class ActorView(View):
    def post(self, request):
        """
        POST /actors/
        新增演员信息
        """
        # 获取所有的请求参数
        params_bytes = request.body
        # 转换成字符串类型
        params_str = params_bytes.decode()
        # 转换成dict
        params = json.loads(params_str)
        # 将数据存放至数据库
        actor = Actor.objects.create(
            aname=params.get('aname'),
            age=params.get('age'),
            agender=params.get('agender'),
            birth_date=params.get('birth_date')
        )

        if actor:
            return JsonResponse({
                'aid': actor.aid,
                'aname': actor.aname,
                'age': actor.age,
                'agender': actor.agender,
                'birth_date': actor.birth_date,
                'photo': actor.photo.url if actor.photo else '',
            }, status=201)

        return HttpResponse(500)

    def get(self, request):
        """
        GET /actors/
        查询所有的演员信息
        """
        acList = Actor.objects.all()
        actorList = []
        for actor in acList:
            actorList.append({
                'aid': actor.aid,
                'aname': actor.aname,
                'age': actor.age,
                'agender': actor.agender,
                'birth_date': actor.birth_date,
                'photo': actor.photo.url if actor.photo else '',
            })
        return JsonResponse(actorList, safe=False)


class ActorDetailView(View):
    def get(self, request, pk):
        """
        GET /actors/pk
        查询某个演员的详情信息
        """
        pk = int(pk)
        try:
            actor = Actor.objects.get(aid=pk)

            return JsonResponse({
                'aid': actor.aid,
                'aname': actor.aname,
                'age': actor.age,
                'agender': actor.agender,
                'birth_date': actor.birth_date,
                'photo': actor.photo.url if actor.photo else '',
            })

        except Actor.DoesNotExist:
            return HttpResponse(status=404)

    def put(self, request, pk):
        """
        PUT /actors/pk
        修改某个演员的信息
        """
        pk = int(pk)
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        # 获取请求参数
        params = json.loads(request.body.decode())

        # 修改演员部分信息
        actor.aname = params.get("aname")
        actor.age = params.get("age")
        actor.save()

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo.url if actor.photo else '',
        }, status=201)

    def delete(self, request, pk):
        """
        DELETE /actors/pk
        删除某个演员的信息
        """
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        actor.delete()

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo.url if actor.photo else '',
        }, status=204)

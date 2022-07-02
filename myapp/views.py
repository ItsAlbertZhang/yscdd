from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timedelta
from myapp.models import Train, TrainClass


def index(request):
    # 发车后的有效时间
    time_effective_mins = 3

    # 获取当前发车信息
    time_now = datetime.now()
    time_effective = timedelta(minutes=time_effective_mins)
    time_earliest = time_now - time_effective
    train_list = Train.objects.filter(train_time__gt=timezone.get_current_timezone().localize(time_earliest), train_capacity__gt=0)
    train_class = TrainClass.objects.all()

    # POST 处理
    if request.method == 'POST':
        try:
            # 尝试在有效的发车信息中找到该 uid
            if train_list.filter(train_uid=request.POST['uid']).exists():
                ob = train_list.filter(train_uid=request.POST['uid']).first()
            else:
                ob = Train()
                ob.train_uid = request.POST['uid']
            ob.train_class = request.POST['class']
            ob.train_capacity = request.POST['capacity']
            ob.train_time = timezone.get_current_timezone().localize(time_now)
            ob.save()
            return redirect(index)
        except:
            return HttpResponse("发车失败!")

    # 返回 templates 模板
    train_list = train_list.filter(train_capacity__gt=0)
    context = {'train_list': train_list, 'train_class': train_class}
    return render(request, 'myapp/index.html', context)

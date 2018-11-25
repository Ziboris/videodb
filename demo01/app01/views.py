from django.shortcuts import render,HttpResponse,get_object_or_404
from app01.models import *
from app01.algorithm.main import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from moviepy.editor import VideoFileClip
from django.urls import reverse
from django.http import HttpResponseRedirect

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.

# class indexItem:
#     choiceNum=0
#     choice=[]
#
# class indexItems:
#     choiceNum=0
#     items=[]

fileNames=[]
material_list = []

# http://www.cnblogs.com/haiyan123/p/9263288.html
def time_convert(size):
    M,H=60,60**2
    if size<=M:
        return str(int(size))+'s'
    elif size<H:
        return '%s m %s s'%(int(size/M),int(size%M))
    else:
        hour=int(size/H)
        mine=int(size%H/M)
        second=int(size%H%M)
        tim_srt='%s h %s m %s s'%(hour,mine,second)
        return tim_srt

def get_video_length(filename):
    clip=VideoFileClip(filename)
    video_length=time_convert(clip.duration)
    return video_length

def index(req):
    # 需要查询到每一个查找属性有多少的选项
    video_list=CVE_Case.objects.all().order_by('case_id')
    paginator=Paginator(video_list,9)
    page=req.GET.get('page')
    videos=paginator.get_page(page)
    context={
        'videos':videos,
    }
    return render(req,'02/02_index.html',locals())

def detail(req,name,case_id):
    video_list=CVE_Case.objects.filter(case_id=case_id)
    video=video_list[0]
    video_tag_list=CVE_Case_Tags.objects.filter(case_id=case_id)
    video_tag=video_tag_list[0]
    shot_list=CVE_Shot.objects.filter(case_id=case_id)

    path=BASE_DIR+'/app01/static/'
    path=os.path.join(path,video.name)
    video_length=get_video_length(path)
    shot_num=len(shot_list)
    return render(req,"02/02_detail.html",locals())


def autoEdit(req):
    root_material_dir='material/'
    global material_list
    path = BASE_DIR + '/app01/static/'+root_material_dir
    list=os.listdir(path)
    cnt=0
    for filename in list:
        cnt = cnt+1
        if cnt==1:
            material_list.append('null')
            cnt=cnt+1
        fullpath=os.path.join(path,filename)
        if os.path.isfile(fullpath):
            material_list.append(root_material_dir+filename)
        if cnt==9:
            cnt=0
    paginator=Paginator(material_list,9)
    page=req.GET.get('page')
    materials=paginator.get_page(page)

    return render(req,"02/02_autoEdit.html",locals())

def delete(req, counter):
    global material_list

    deleteName=material_list[counter]
    fullName=os.path.join(BASE_DIR,"app01","static",deleteName)
    os.remove(fullName)
    # return HttpResponseRedirect(reverse('autoEdit'))
    return HttpResponseRedirect(reverse('autoEdit'))

def para(req):
    global fileNames
    objs = req.FILES.getlist("fileUpload")
    for obj in objs:
        fileNames.append(obj.name)
        f = open(os.path.join(BASE_DIR, 'app01', 'static', 'material', obj.name), 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
    return render(req,"02/02_para.html",locals())

def download(req):
    editedVideo=EditedVideo()
    shotElement=ShotElement()

    if req.method == "POST":
        editedVideo.speedArg=int(req.POST.get("speedArg_options")) #主体运动变化，运动/平稳 1/0 大/小
        editedVideo.positionArg=int(req.POST.get("positionArg_options"))#主体位置变化，一致/不一致 0/1 小/大
        editedVideo.cramArg= int(req.POST.get("cramArg_options")) #镜头运动变化，运动/平稳 1/0 大/小
        editedVideo.colorArg= int(req.POST.get("colorArg_options")) #画面色调变化，一致/对比 0/1 小/大
        editedVideo.jumpArg=int(req.POST.get("jumpArg_options")) #跳剪，是、否 1/0 大/小

        # 首尾镜头：主体运动强度 强-2 中-1 弱-0
        shotElement.speed.append(int(req.POST.get("start_speed_options")))
        shotElement.speed.append(int(req.POST.get("end_speed_options")))
        # 首尾镜头：镜头运动强度 强-2 中-1 弱-0
        shotElement.craMotion.append(int(req.POST.get("start_craMotion_options")))
        shotElement.craMotion.append(int(req.POST.get("end_craMotion_options")))
        # 首尾镜头：画面主体位置 强-2 中-1 弱-0
        shotElement.position.append(int(req.POST.get("start_position_options")))
        shotElement.position.append(int(req.POST.get("end_position_options")))
        # 首尾镜头：画面色调 暖-2 中-1 冷-0
        shotElement.color.append(int(req.POST.get("start_color_options")))
        shotElement.color.append(int(req.POST.get("end_color_options")))

        editedVideo.shots.append(shotElement)

        split1,split2=req.POST.get("myslider").split(',')
        split1=float(split1)
        split2=float(split2)
        timeTemplete=[]    #???怎么传递
        timeTemplete.append('%.2f' % (split1/100.0))
        timeTemplete.append('%.2f'%  (split2/100.0-split1/100.0))
        timeTemplete.append('%.2f' %(1.0-split2/100.0))
        #运算：生成视频---存入数据库（结构体）
        #               ---放到案例目录下(函数生成的默认放到的是当前目录下）
        #               ---提供下载功能

        produce=VideoMerge(fileNames, timeTemplete, editedVideo)
        CVE_Case.objects.create(name=produce,jumpArg=editedVideo.jumpArg,speedArg=editedVideo.speedArg,positionArg=editedVideo.positionArg,cramArg=editedVideo.cramArg,colorArg=editedVideo.colorArg)
        video_id=CVE_Case.objects.filter(name=produce)[0].case_id
        CVE_Shot.objects.create(case_id=video_id,speed=shotElement.speed,position=shotElement.position,craMotion=shotElement.craMotion,color=shotElement.color)

        fread=open(os.path.join(BASE_DIR,'templates','02',produce),'rb')
        for line in fread:
            with open(os.path.join(BASE_DIR, 'app01', 'static',produce), 'wb') as fwrite:
                fwrite.write(line)
        tempProduce="2.mp4"

    return render(req,"02/02_download.html",locals())

def tag(req):
    return render(req,"02/02_tag.html",locals())

def contactus(req):
    return render(req,"02/02_contactus.html",locals())

# def repo_base(req):
#     #读取所有的视频文件 model 检索功能
#     video_list = CVE_Case.objects.all()
#     flag=False
#     search = ""
#     if req.method == "POST":
#         search=req.POST.get("search")
#         flag=True
#
#
#
#     return render(req, "repo_base.html", locals())
#
#
#
# #-----
# def repo_1(req):
#     #只针对该功能的检索视频结果展示
#     video_list=CVE_Case_Tags.objects.order_by('product_type')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_1.html",locals())
#
# def repo_2(req):
#     #只针对该功能的检索视频结果展示
#     video_list = CVE_Case_Tags.objects.order_by('product_style')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_2.html",locals())
#
# def repo_3(req):
#     #只针对该功能的检索视频结果展示
#     video_list = CVE_Case_Tags.objects.order_by('busi_orientation')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_3.html",locals())
#
# def repo_4(req):
#     #只针对该功能的检索视频结果展示
#     video_list = CVE_Case_Tags.objects.order_by('media')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_4.html",locals())
#
# def repo_5(req):
#     #只针对该功能的检索视频结果展示
#     video_list = CVE_Case_Tags.objects.order_by('year')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_5.html",locals())
#
# def repo_6(req):
#     #只针对该功能的检索视频结果展示
#     video_list = CVE_Case_Tags.objects.order_by('consumer')
#     video_list2 = CVE_Case.objects.all()
#     return render(req,"repo_6.html",locals())
# #-----
#
#
#
# def case_change(req):
#     # 这里req的内容 应该是从之前提交过来的
#     # 这里直接写死 name和id
#     videoId=1
#     videoName="video1.avi"
#     # 根据内容去数据库里面取
#     video=CVE_Case.objects.filter(case_id=videoId)
#     shot_list=CVE_Shot.objects.filter(case_id=videoId)
#     return render(req,"case_change.html",locals())
#
# def upload_material(req):
#     caseId=0
#     case=0
#     caseName=""
#     materialName=""
#     if  req.method == 'GET':
#         caseId=req.GET.get("id")
#         print(caseId)
#         case=CVE_Case.objects.filter(case_id=caseId)
#         caseName=case[0].name
#         return render(req,"upload_material.html",locals())
#     elif req.method == "POST":
#         obj=req.FILES.get("fileUpload")
#         caseName=req.POST.get("caseName")
#         materialName=obj.name
#         f=open(os.path.join(BASE_DIR,'templates','pic',obj.name),'wb')
#         for line in obj.chunks():
#             f.write(line)
#         f.close()
#         return render(req,"upload_material.html",locals())
#
# def analyzing(req):
#     return render(req,"analyzing.html",locals())
#
#
#
#
# def display_case_parameter(req):
#     global caseName
#     global case_list
#     global editedVideo
#     global shot_list
#     global startShot
#     global endShot
#     global materialName
#
#     if req.method == 'GET':
#         caseName=req.GET.get("caseName")
#         materialName=req.GET.get("materialName")
#         print("casename:" + caseName)
#         case_list=CVE_Case.objects.filter(name=caseName)
#     elif req.method == 'POST':
#         ans=VideoMerge(materialName,0,EditedVideo)
#         return render(req,"download_material.html",locals())
#
#
#     if len(case_list) ==0: #说明不在库里面 需要重新分析并且上传到库文件
#         pass
#     elif len(case_list)>0: #直接从库里面取出来就可以了
#         caseId=case_list[0].case_id
#         shots=CVE_Shot.objects.filter(case_id=caseId)
#         startShot=shots[0]
#         endShot=shots[len(shots)-1]
#         # print(type(startShot))
#         # print(len(shots))
#         for shot in shots:
#             shot_list.append(ShotElement(shot.shot_id,shot.start,shot.end,shot.during,shot.speed,shot.position,shot.craMotion,shot.color,shot.shotSize))
#         editedVideo=EditedVideo(case_list[0].case_id,case_list[0].name,case_list[0].jumpArg,case_list[0].speedArg,case_list[0].positionArg,case_list[0].cramArg,case_list[0].colorArg,shot_list)
#
#
#     return render(req, "display_case_parameter.html", globals())
#
#
# #=====test======
# def show(req):
#     video_list=CVE_Case.objects.all()
#     paginator=Paginator(video_list,3)
#
#     page=req.GET.get('page')
#     try:
#         videos=paginator.page(page)
#     except PageNotAnInteger:
#         #if page is no an integer,deliver first page
#         videos=paginator.page(1)
#     except EmptyPage:
#         # if page is out of range(e.g. 9999) ,deliver last pagr of the result
#         videos=paginator.page(paginator.num_pages)
#
#     return render(req,'test/show.html',{'videos':videos})
#
#
# def test1(req):
#     # return render(req,"test/test1.html")
#     video_list=CVE_Case.objects.all().order_by("case_id")
#     paginator=Paginator(video_list,4)
#     page=req.GET.get("page")
#     videos=paginator.get_page(page)
#     context={
#         'videos':videos,
#     }
#     print("ok")
#     return render(req,'test/test1.html',context)
#
# def test2(req):
#     pass
#
# def test3(req):
#     pass


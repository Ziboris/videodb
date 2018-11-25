#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = ' 2018/11/5 15:29'
__author__ = 'ziboris'

class ShotElement():
    id = 0
    start = 0  # 镜头起始帧
    end = 0  # 镜头结束帧
    during = 0  # 镜头属性0，时长
    speed = []  # 镜头属性1，主体运动状态
    position = []  # 镜头属性2，主体位置
    craMotion = []  # 镜头属性3，镜头运动状态
    color = []  # 镜头属性4，色调
    shotSize = 0  # 镜头属性5，景别
    # def __init__(self, id, start, end, during, speed, position, craMotion, color, shotSize):
    #     self.id = id
    #     self.start = start
    #     self.end = end
    #     self.during = during
    #     self.speed = speed
    #     self.position = position
    #     self.craMotion = craMotion
    #     self.color = color
    #     self.shotSize = shotSize

class EditedVideo():
    id = 0
    name = ""  # 视频名
    jumpArg = 0  # 组接参数1，跳剪，是、否 1/0 大/小
    speedArg = 0  # 组接参数2，主体运动状态，运动/平稳 1/0 大/小
    positionArg = 0  # 组接参数3，主体位置，一致/不一致 0/1 小/大
    cramArg = 0  # 组接参数4，镜头运动状态，运动/平稳 1/0 大/小
    colorArg = 0  # 组接参数5，色调，一致/对比 0/1 小/大
    shots = [ShotElement]  # 所有镜头属性

    # def __init__(self, id, name, jumpArg, speedArg, positionArg, cramArg, colorArg, shots):
    #     self.id = id
    #     self.name = name
    #     self.jumpArg = jumpArg
    #     self.speedArg = speedArg
    #     self.positionArg = positionArg
    #     self.cramArg = cramArg
    #     self.colorArg = colorArg
    #     self.shots = shots


def videoAnalysis(videoName):           #视频组接属性检测
    #videoName string
    shot = ShotElement(0,0,0,0,0,[],[],[],[],[],[])
    shots = []
    shots.append(shot)
    return EditedVideo(0,videoName,0,0,0,0,0,shots)


def VideoMerge(fileNames,timeTemplete,editedVideo):       #自动视频组接
    #timeTemplete list
    #editedVideo EditedVideo

    return "produce.mp4"           #return string

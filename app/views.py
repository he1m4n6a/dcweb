# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect,HttpResponse

import os
import uuid
import json
import datetime as dt
import hashlib
import random
import requests
import time
import logging


# 项目名字
Project = "app"
# 修改成自己的主机地址
Host = "http://localhost:8888"

# 日志记录
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='log/scan.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def index(request):
    return HttpResponseRedirect("/upload")

def report(request, rid):
    return render(request, 'report/%s.html' %rid)

def illegalFileName(filename):
    dangerChars = [';','|','"',"'",'&','^','%','$','@']
    for c in dangerChars:
        if c in filename:
            return True    
    return False

def upload_files(request):
    if request.method == "POST":           
        f = request.FILES.get("uploadfile")
        if f:
            # 设置白名单后缀
            allow_suffix = ['tar', '7z', 'zip', 'gz', 'war', 'so', 'rar', 'bz2', 'arj', 'cab', 'lzh','iso', 'UUE', 'jar']
            file_suffix = f.name.split(".")[-1].lower()        
            if file_suffix not in allow_suffix: 
                return render(request, 'uploadfile.html', {'warning': '文件格式错误，请重新上传！'})
            if illegalFileName(f.name):
                 return render(request, 'uploadfile.html', {'warning': '文件名非法，请重新上传！'})
            pwd = os.path.abspath('.') 
            uploaddir = os.path.abspath('.') + os.sep + 'app/files'
            today = dt.datetime.today()
            dir_name = uploaddir + '/%d/%d/' % (today.year, today.month)
            filename = os.path.join(uploaddir, dir_name, f.name)   
            if not os.path.exists(dir_name):  
                os.makedirs(dir_name)
            # 保存文件
            try:
                fobj = open(filename, 'wb') 
                for chrunk in f.chunks():
                    fobj.write(chrunk)     
                fobj.close()
            except Exception as e:
                print str(e)
            firstname = f.name.split('.')[0]
            fr = open(filename, 'r').read()
            md5file = hashlib.md5(fr).hexdigest()
            output = 'tmp_' + md5file + '.html'
            # 执行第三方依赖库的分析
            try:
                logging.info('[+] 开始扫描%s项目, 文件md5值是%s' %(firstname, md5file))
                shell = './dependency-check/bin/dependency-check.sh --project "%s" --scan "%s" -o %s' %(firstname, filename, output)
                print shell
                os.system('./dependency-check/bin/dependency-check.sh --project "%s" --scan "%s" -o %s' %(firstname, filename, output))
                logging.info('[+] %s项目扫描结束, 文件md5值是%s' %(firstname, md5file))
            except Exception as e:
                print str(e)
                logging.info('[-] %s项目扫描出错, 文件md5值是%s' %(firstname, md5file))
                return render(request, 'uploadfile.html', {'error': '命令执行错误，请联系管理员！'})                

            # 网页形式report
            absfilename = pwd + os.sep + output
            absreport = pwd + os.sep + Project + os.sep + 'templates' + os.sep + 'report'
            if not os.path.exists(absreport):
                os.makedirs(absreport)
            absmd5name = absreport + os.sep + md5file + '.html'
            try:
                os.system('mv %s %s' %(absfilename, absmd5name))
            except Exception as e:
                logging.info('[-] %s项目扫描出错, 文件md5值是%s' %(firstname, md5file))
                return render(request, 'uploadfile.html', {'error': '命令执行错误，请联系管理员！'})                
            report_addr = Host + os.sep +  'report' + os.sep + md5file
            return render(request, 'uploadfile.html', {'success':report_addr})
        else:
            return render(request, 'uploadfile.html', {'warning': '请先选择需要上传的文件！'})
 
    else:
        return render(request,'uploadfile.html')

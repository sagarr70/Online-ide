from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
import sys
import os
import subprocess
import shutil
# Create your views here.
def greetings(request):
    print("hello")
    res = render(request,'codestar/home.html')
    return res
@csrf.csrf_exempt
def runcode(request):
    print("runninggggggggggggggggggg")
    if request.method == 'POST':
        language= request.POST['language']
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        print(language)
        print(input_part)
        print(code_part)
        if (language=='cpp'):
            with open("one.cpp",'w') as file:
                file.write(code_part)
                file.close()
            temp_path=os.getcwd()
            print(temp_path)
            # input_part = input_part.replace("\n","")
            os.system('type nul > input.txt')
            with open("input.txt",'w') as file:
                file.write(input_part)
                file.close()
            # subprocess.run(['g++','one.cpp'])
            # os.system('g++ one.cpp')
            error=subprocess.run(['g++','one.cpp'], capture_output=True,shell=True)
            success=True
            if(error.stderr.decode('UTF-8')!=''):
                result=error.stderr.decode('UTF-8')
                success=False
            else:
                result=subprocess.run(['a.exe','<','input.txt'], capture_output=True,shell=True)
                result=result.stdout.decode('UTF-8')
            # os.system('a.exe < input.txt > output.txt')
            # with open ("output.txt", "r") as myfile:
                #  result=myfile.read()
            # if(result2==''):
                # result=result.stderr.decode('UTF-8')
            # print(result)

            # os.remove('output.txt')
            # if(success):
            #   os.remove('a.exe')
            
            # res = render(request,'codestar/home.html',{"code":code_part,"input":input_part,"output":result})
            res = HttpResponse(result)

        if (language=='py'):
            y = input_part
            input_part = input_part.split('\n')
            def input():
                a = input_part[0]
                del input_part[0]
                return a
            try:
                orig_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w')
                exec(code_part)
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = open('file.txt', 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = e
            print(output)
            # res = render(request,'codestar/home.html',{"code":code_part,"input":y,"output":output})
            res = HttpResponse(output)
    return res
def report(request):
    res =render(request,'codestar/report.html')
    return res
from django.shortcuts import render
import pickle

# Create your views here.

def home(request):
    return render(request,'home.html')

def result(request):

    cls = pickle.load(open('AI_Sheet.pkl', 'rb'))

    lis = []

    lis.append(float(request.GET['a']))
    lis.append(float(request.GET['b']))
    lis.append(float(request.GET['c']))
    lis.append(float(request.GET['d']))
    lis.append(float(request.GET['e']))
    lis.append(float(request.GET['f']))
    
    pred = cls.predict([lis])

    return render(request,'result.html',{'data':pred})

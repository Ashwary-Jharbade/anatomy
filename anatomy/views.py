from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter
import pickle


from .models import UserProfile, SequenceTest ,TestHistory

@login_required
def history(request):
    hobj = TestHistory.objects.filter(user = request.user).order_by('-date')
    return render(request,'history.html',{'obj':hobj})

@login_required
def dashboard(request):
    return render(request,'userDashboard.html')

@login_required
def sequence(request):
    if request.method == 'POST':
        file = request.FILES['filename']
        obj = SequenceTest(user = request.user, file = file)
        obj.save()

        try:
            strname = obj.file.path
            ncov_record = []
            for i in SeqIO.parse(strname,"fasta"):
                ncov_record = i
            ncov_recordSeq = SeqIO.read(strname,"fasta")
            ncov_dna = ncov_recordSeq.seq
            sequenceLength = len(ncov_recordSeq.seq)
            ncov_mrna = ncov_dna.transcribe()
            mrnaLength = len(ncov_mrna)
            ncov_protein = ncov_mrna.translate()
            proteinSequenceLength = len(ncov_protein)
            ncov_aa = ncov_protein.split("*")
            ncov_clean = [str(i) for i in ncov_aa]
            commonProteins = Counter(ncov_protein).most_common()
            dic = {}
            for i in commonProteins:
                dic[i[0]] = i[1]
        except Exception as e:
            print(e)
        try:
            lis = [dic[i] for i in dic]
            f = open('anatomy//my_NewClassifier.pickle', 'rb')
            classifier = pickle.load(f)
            predicted = classifier.predict([lis])[0]
            data = {"res":"Success","predicted":predicted,"id":ncov_record.id,"recordname":ncov_record.name,"description":ncov_record.description,"features":0,"sequencelength":sequenceLength,"mrnalength":mrnaLength,"proteinsequencelength":proteinSequenceLength,"L":dic["L"],"S":dic["S"],"*":dic["*"],"T":dic["T"],"C":dic["C"],"F":dic["F"],"R":dic["R"],"V":dic["V"],"Y":dic["Y"],"N":dic["N"],"I":dic["I"],"K":dic["K"],"G":dic["G"],"A":dic["A"],"H":dic["H"],"Q":dic["Q"],"P":dic["P"],"D":dic["D"],"E":dic["E"],"W":dic["W"],"M":dic["M"]}

            testreport = "Negative"
            if predicted:
                testreport = "Positive"
            TestHistory(user = request.user,sfile = obj,result=testreport,sequenceid=ncov_record.id,sequencefeature=0,dnaseqlength=sequenceLength,mrnasequencelength=mrnaLength,proteinSequenceLength=proteinSequenceLength,L=dic["L"],S=dic["S"],T=dic["T"],C=dic["C"],F=dic["F"],R=dic["R"],V=dic["V"],Y=dic["Y"],N=dic["N"],I=dic["I"],K=dic["K"],G=dic["G"],A=dic["A"],H=dic["H"],Q=dic["Q"],P=dic["P"],D=dic["D"],E=dic["E"],W=dic["W"],M=dic["M"]).save()
        except Exception as e:
            print(e)
            return render(request,'userDashboard.html',{"res":"Failed"})
        return render(request,'userDashboard.html',data)
    return render(request,'userDashboard.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        selecteduser = authenticate(username = username,password = password)
        if selecteduser:
            if selecteduser.is_active:
                login(request,selecteduser)
                return redirect('/dashboard/')
            else:
                return HttpResponse("<h1>User deactivated</h1>")
        else:
            return render(request,'signin.html',{'filler':'Alert : Email or Password does not match try again'})
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        try:
            mobile = request.POST['mobile']
            username = request.POST['email']
            password = request.POST['password']
            uobj = User(username=username)
            uobj.save()
            uobj.set_password(password)
            uobj.save()
            upobj = UserProfile(user=uobj,mobile=mobile)
            upobj.save()
        except Exception as e:
            print(e)
    return render(request,'signup.html')

@login_required
def signout(request):
    logout(request)
    return redirect('/')

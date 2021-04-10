from django.shortcuts import render,redirect
import yfinance as yf
from django.contrib import messages

# Create your views here.
def homepageview(request):
    return render(request,'homepage.html')


def graphview(request):
    company = request.POST['company']
    df = yf.Ticker(company)
    df = df.history(period="1mo", interval="1d")['Close']
    print(df)
    dates = []
    values = []
    for i in df.index:
        dates.append(i.date())
        values.append(df[i])
    print(dates)
    print(values)
    if values == []:
        messages.add_message(request, messages.INFO, 'Company Not Found')
        return redirect('homepageview')

    context = {'company' : company,'dates':dates,'values':values}


    return render(request,'graph.html',context)
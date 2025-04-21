from django.shortcuts import render

def converter(request):
    context = {}
    if request.method == "POST":
        amount = float(request.POST.get('amount', 0))
        conversion_type = request.POST.get('conversion')
        if conversion_type == 'usd_to_inr':
            result = round(amount * 83, 2)
            context['result'] = f"{amount} USD = {result} INR"
        elif conversion_type == 'inr_to_usd':
            result = round(amount / 83, 2)
            context['result'] = f"{amount} INR = {result} USD"
    return render(request, 'app4/converter.html', context)

def timer(request):
    return render(request, 'app4/timer.html')

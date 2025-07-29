from django.shortcuts import render

def calculator(request):
    return render(request, 'calculator.html')
    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        operator = request.POST.get('operator')

        if operator == 'Addition':
            result = a + b
        elif operator == 'Subtraction':
            result = a - b
        elif operator == 'Multiplication':
            result = a * b
        elif operator == 'Division':
            result = a / b

    context = {'result': result}
    return render(request, 'calculator.html', context)

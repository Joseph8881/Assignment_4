from django.shortcuts import render
from .forms import InputForm
import math

def calculator_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            # Condition 1
            if a < 1:
                error = "Value A is too small."
            
            # Condition 2
            elif c < 0:
                error = "Value C cannot be negative."

            else:
                c_cubed = c ** 3

                sqrt_value = math.sqrt(c_cubed)

                if c_cubed > 1000:
                    final = sqrt_value * 10
                else:
                    final = sqrt_value / a

                if b == 0:
                    result = f"B is zero. Final result: {final}"
                else:
                    final += b
                    result = f"Final result: {final}"
        else:
            error = "Invalid input. Please enter numeric values."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })
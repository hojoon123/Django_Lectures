from django.shortcuts import render

# Create your views here.
def example_view(request):
    # first_app/templates/first_app/example.html
    return render(request,'first_app/example.html')


def variable_view(request):
    
    my_var = {'first_name':'k', 'last_name' : 'HJ',
              'some_list' : [1,2,3], 'some_dic' : {'inside_key' :'inside_value'},
              'user_logged_in': True,
    }
    
    return render(request,'first_app/variable.html', context= my_var)
import json


import requests as r

from django.shortcuts import render

from .forms import InputForm

from django.http import HttpResponse


'''some functionalities are not implemented yet, like keeping the user details in database and also showing results 
of search part, and also automatic generation of email messages, we  have just written the code but not yet implemented them here, given some time we will
finish this fully'''

market={"data":"data","data1":"data1","data2":"data2","data3":"data3","data4":"data4","data5":"data5"}

base_url = "https://api.openai.com/v1/"

key = "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"

header = {"Content_Type": "application/json", "Authorization": "Bearer {}".format(key)}

message=[]


data = {
      
        'model': 'gpt-3.5-turbo-0613',

        "messages":message

    }








def create_introduction():
       
       message.append({"role": "user", "content": "Write an introduction to welcome users to my websites of exports and import information,in ten words"})

       response=generate_message()

       return response

def generate_message():
        
        try:
         
         response=r.post(base_url+"chat/completions",headers=header,json=data).text

         full_response=json.loads(response)

         answer=full_response["choices"][0]["message"]

         message.append(answer)

         print("in 1")

         return answer['content']
        
        except Exception:
         
         try:
          
          second_key ='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'

          second_header ={"Content_Type": "application/json", "Authorization": "Bearer {}".format(second_key)}
         
          response=r.post(base_url+"chat/completions",headers=second_header,json=data).text

          full_response=json.loads(response)

          answer=full_response["choices"][0]["message"]

          message.append(answer)

          print("in 2")

          return answer['content']
         
         except Exception:
               
               print("in 3") 
               print(response)

               return generate_message()
               


        
 

def find_market(product):

        message.append({"role":"user","content":"in which country has high demand of "+product+" ,in just one word"})

        response=generate_message()

        return response


def importer():

        message.append({"role":"user","content":"list five potential importers i should get contact to, or who should i contact and should include their public bussiness contact details if they have,real details not fictional enough"})

        response=generate_message()

        market["data3"]=response

        return response


def demad_level(product):
      
      message.append({"role":"user","content":"What is the level od demand of "+product+" in this country?, just in one paragraph"})

      response=generate_message()
      
      market['data']=response

      return response 


def find_cost(product, quantity):

        message.append({"role":"user","content":"what is the best price to sell "+product+" for "+quantity+",just approximate the general price  , in just one paragraph"})

        response=generate_message()
        
        market["data1"]=response

        return response


def transport_network(country,product):

        message.append({"role":"user","content":"to export from "+country+" to the importers country, which transport network the is best"+product+",in just one paragraph"})

        response=generate_message()
        
        market["data2"]=response

        return response


def legal_requirements(product):

        message.append({"role":"user","content":"what are the legal requirements for selling "+product+" ,make it brief and detailed"})

        response=generate_message()
        
        market["data4"]=response

        return response


def general_advise(product,quantity):

        message.append({"role":"user","content":"I have decided to export "+quantity+" of "+product+" in this country and i would like some advise, make it brief and clear"})

        response=generate_message()
        
        market["data5"]=response

        return response       
              
 
def HomePage(request):  
    
    content =create_introduction()

    return render(request, "HomePage.html", {"content": content})


def exports(request):
    
    return render(request, "Exports.html")

def Results(request):
     if request.method == 'POST':
          form = InputForm(request.POST)
          if form.is_valid():
                user_country = form.cleaned_data['Country']
                user_product = form.cleaned_data['product']
                user_quantity = form.cleaned_data['quantity']
               
                find_market(user_product)

                demad_level(user_product)

                find_cost(user_product,user_quantity)

                transport_network(user_country,user_product)

                importer()

                legal_requirements(user_product)

                general_advise(user_product,user_quantity)
                
                return render(request, "Results.html",{"data":market["data"], "data2":market["data1"], "data3":market["data2"], "data4":market["data3"], "data5":market["data4"], "data6":market["data5"]})
                




def imports(request):
       
       return render(request,'Imports.html')


def imports(request):
    return render(request, 'Imports.html')

def sign_up(request):
     return render(request,'sign_up.html')



def sign_in(request):
     return render(request,'sign_in.html')
     

def news(request):
    try:
        api_key = '72c28953a906487f92794a802e1439a6'

        endpoint = 'https://newsapi.org/v2/everything'
        params = {
            'apiKey': api_key,
            'q': 'imports exports trade commerce',
            'language': 'en'
        }

        response = r.get(endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            data = data['articles']
            return render(request, 'news.html', {"data": data})
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return HttpResponse(status=500)  # Return a 500 Internal Server Error response

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return HttpResponse(status=500)
    

def search_page(request):
     return render(request,'search_page.html')

def table(request):
     return render(request,'table.html')
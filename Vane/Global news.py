# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:47:14 2023

@author: user
"""
import requests

api_key = '72c28953a906487f92794a802e1439a6'

endpoint = 'https://newsapi.org/v2/everything'   #this is the endpoint URL for the top headlines

params = {
    'apiKey': api_key,
    'q': 'imports exports trade commerce',  # Keywords related to imports and exports
    'language': 'en'
}




def news(request):
    try:

        response = requests.get(endpoint, params=params)  #here there is an API request

        
        if response.status_code == 200:     # Check if the request was successful (status code 200)
            
            data = response.json()
            return data['articles']


        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "No response"
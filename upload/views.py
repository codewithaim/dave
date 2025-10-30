from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

import pandas as pd
import json

# Create your views here.
def home(request):
    if request.method == "POST":
        old_data = Data.objects.all()
        old_data.delete()

        filename = request.FILES['filename']
        file_df = pd.read_csv(filename)

        # Save the file into a json format to prepare for loading into DB
        json_records = file_df.reset_index().to_json(orient="records")
        data = []
        data = json.loads(json_records)
        
        for rec in data:
            property_name = rec['property_name']
            property_price = rec['property_price']
            property_rent = rec['property_rent']
            emi = rec['emi']
            tax = rec['tax']
            other_exp = rec['other_exp']
            monthly_expenses = emi+tax+other_exp
            monthly_income = property_rent - monthly_expenses

            dt = Data(
                property_name = property_name,
                property_price = property_price,
                property_rent = property_rent,
                emi = emi,
                tax = tax,
                other_exp = other_exp,
                monthly_expenses = monthly_expenses,
                monthly_income = monthly_income
            )
            dt.save()
        
        data_objects = Data.objects.all()
        context = {
            "data_objects": data_objects
        }
        return render(request, "upload/index.html", context)
    else:
        print("This is a get request")    
            
    return render(request, "upload/index.html")

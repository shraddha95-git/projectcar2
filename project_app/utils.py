
import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class OutletSales():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier):
        self.Item_Weight=Item_Weight
        self.Item_Fat_Content=Item_Fat_Content
        self.Item_Visibility=Item_Visibility
        self.Item_MRP=Item_MRP
        self.Outlet_Establishment_Year=Outlet_Establishment_Year
        self.Outlet_Size=Outlet_Size
        self.Outlet_Location_Type=Outlet_Location_Type
        self.Outlet_Type=Outlet_Type

        self.Item_Type= "Item_Type_" + Item_Type
        self.Outlet_Identifier= "Outlet_Identifier_" + Outlet_Identifier



    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):

        self.load_model()   # Creating instance of model and json_data
        Item_Type_index =        list(self.json_data['columns']).index(self.Item_Type)
        Outlet_Identifier_index =list(self.json_data['columns']).index(self.Outlet_Identifier)

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Item_Weight
        test_array[1] = self.json_data['Item_Fat_Content'][self.Item_Fat_Content]
        test_array[2] = self.Item_Visibility
        test_array[3] = self.Item_MRP
        test_array[4] = self.Outlet_Establishment_Year
        test_array[5] = self.json_data['Outlet_Size'][self.Outlet_Size]
        test_array[6] = self.json_data['Outlet_Location_Type'][self.Outlet_Location_Type]
        test_array[7] = self.json_data['Outlet_Type'][self.Outlet_Type]
        test_array[Item_Type_index] = 1
        test_array[Outlet_Identifier_index]=1

        print("Test Array -->\n", test_array)

        charges = round(self.model.predict([test_array])[0],2)

        return charges

if __name__ == "__main__":
    Item_Weight= 65
    Item_Fat_Content='Regular'
    Item_Visibility=0.016760
    Item_MRP=249.809
    Outlet_Establishment_Year=1999
    Outlet_Size='Medium'
    Outlet_Location_Type='Tier 2'
    Outlet_Type='Grocery Store'
    Item_Type = 'Breads'
    Outlet_Identifier= 'OUT010'

    Object = OutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier)

    charges = Object.get_predicted_charges()
    print("Predicted Charges:", charges, "/- Rs.")

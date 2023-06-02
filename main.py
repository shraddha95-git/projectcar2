from flask import Flask, jsonify, render_template, request

from project_app.utils import OutletSales

app=Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Welcome to outlet Sales prediction system")   
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_outletsales_charges():
    if request.method == "GET":
        print("We are in a GET Method")

        Item_Weight =    eval(request.args.get("Item_Weight"))
        Item_Fat_Content=request.args.get("Item_Fat_Content")
        Item_Visibility =eval(request.args.get("Item_Visibility"))
        Item_MRP =eval(request.args.get("Item_MRP"))
        Outlet_Establishment_Year = eval(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Outlet_Type = request.args.get("Outlet_Type")
        Item_Type = request.args.get("Item_Type")
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        

        print("***************** Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier********************\n",Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier)

        Object = OutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier)
        charges =  Object.get_predicted_charges()

        return render_template("index.html", prediction = charges)
    
    print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters





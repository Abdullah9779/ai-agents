import json

with open("data.json") as file:
        data = json.load(file)

def get_order_status(oder_id):
    for i in data["data"]:
        if i["id"] == oder_id:
            return f"Order Id : {i["id"]} -- Name : {i["name"]} -- Status : {i["status"]} -- Order place Date : {i["order_data"]}"
    else:
        return "Invalid or wrong Order Id"
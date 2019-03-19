import json

class JSONbill:
    """
    write data of orders into json files
    """

    def write_json(self, id_order ,saleman_id, beverage_to_bill, ingredient_to_bill, beverage_price):
        """ write data to json"""
        path = r'C:\Users\Dell\PycharmProjects\coffeeforme\bills\'' + '[ bill #' + str(id_order)  + ']' + '.json'
        filePathNameWExt = path.replace("\\\\","\\")
        with open(filePathNameWExt, 'a') as f:
            data = {"Order #":id_order, 'Saleman id #':saleman_id, 'Beverage type': beverage_to_bill,
                    'Ingredents':ingredient_to_bill, 'Total price':beverage_price}
            json_data = json.dump(data,f)


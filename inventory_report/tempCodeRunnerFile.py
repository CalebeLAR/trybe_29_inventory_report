
jsonImporter = JsonImporter()
lista = jsonImporter.import_data("inventory_report/data/inventory.json")
print(repr(lista[0]))
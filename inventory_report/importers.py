import json
from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product


# interface
class Importer(ABC):
    @abstractmethod
    def import_data(self, path_file: str) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self, path_file: str) -> List[Product]:
        with open(path_file, "r") as jsonFile:
            products_data = json.load(jsonFile)
            # usa o "desempacotamento" ou "unpacking" do python para passar
            # dos os valores de cada produto em products_data
            return [Product(*product.values()) for product in products_data]


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

# jsonImporter = JsonImporter()
# lista = jsonImporter.import_data("inventory_report/data/inventory.json")
# print(repr(lista[0]))

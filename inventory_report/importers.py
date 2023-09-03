import json
from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product


# interface
class Importer(ABC):
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> List[Product]:
        with open(self.path, "r") as jsonFile:
            products_data = json.load(jsonFile)
            # usa o "desempacotamento" ou "unpacking" do python para passar
            # dos os valores de cada produto em products_data
            return [Product(*product.values()) for product in products_data]


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

# jsonImporter = JsonImporter("inventory_report/data/inventory.json")
# lista = jsonImporter.import_data()
# print(repr(lista[0]))

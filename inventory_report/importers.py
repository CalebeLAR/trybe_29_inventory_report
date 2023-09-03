import json
import csv
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
            prod_data = json.load(jsonFile)
            # usa o "desempacotamento" ou "unpacking" do python para passar
            # dos os valores de cada produto em prod_data
            return [Product(*product.values()) for product in prod_data]


class CsvImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> List[Product]:
        with open(self.path, encoding="utf-8", newline="") as csvfile:
            _, *prod_data = csv.reader(csvfile, delimiter=",", quotechar='"')
            # usa o "desempacotamento" ou "unpacking" do python para passar
            # dos os valores de cada produto em prod_data
            return [Product(*product) for product in prod_data]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

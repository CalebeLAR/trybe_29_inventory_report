# from typing import Type
# from inventory_report.importers import JsonImporter
from inventory_report.product import Product

PATH = "inventory_report/data/inventory.json"


class Inventory:
    def __init__(self, data: list[Product] | None = None) -> None:
        self.__data = [] if not data else data

    def add_data(self, data: list[Product]) -> None:
        self.__data.extend(data)

    @property
    def data(self) -> list[Product]:
        return self.__data

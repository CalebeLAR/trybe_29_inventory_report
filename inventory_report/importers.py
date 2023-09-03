from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product


# interface
class Importer(ABC):
    @abstractmethod
    def import_data(self, path_file: str) -> List[Product]:
        pass


class JsonImporter:
    pass


class CsvImporter:
    pass


# Não altere a variável abaixo

# IMPORTERS: Dict[str, Type[Importer]] = {
#     "json": JsonImporter,
#     "csv": CsvImporter,
# }

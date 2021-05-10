import datetime
from typing import List, Dict


class Delito:

    def __init__(self, data: dict):

        self.delito: str = self.__fetch_attribute(name='delito', data=data)
        self.sub_delito: str = self.__fetch_attribute(name='subdelito', data=data)
        self.fecha: datetime.datetime = self.__convert_text_to_date(self.__fetch_attribute(name='fecha', data=data))
        self.victima: str = self.__fetch_attribute(name='victima', data=data)
        self.sub_victima: str = self.__fetch_attribute(name='subvictima', data=data)
        self.edad:str = self.__fetch_attribute(name='edad', data=data).upper()
        self.genero: str = self.__fetch_attribute(name='genero', data=data)
        self.nacionalidad: str = self.__fetch_attribute(name='nacionalidad', data=data)
        self.provincia: str = self.__fetch_attribute(name='provincia', data=data)
        self.canton: str = self.__fetch_attribute(name='canton', data=data)
        self.distrito: str = self.__fetch_attribute(name='distrito', data=data)

    def as_dict(self):
        return {
            "delito": self.delito,
            "sub_delito": self.sub_delito,
            "fecha": f"{self.fecha.day}/{self.fecha.month}/{self.fecha.year}",
            "victima": self.victima,
            "sub_victima": self.sub_victima,
            "edad": self.age_as_range(),
            "genero": self.genero,
            "nacionalidad": self.nacionalidad,
            "provincia": self.provincia,
            "canton": self.canton,
            "distrito": self.distrito
        }

    def __str__(self) -> str:
        return str(self.as_dict())

    @staticmethod
    def __fetch_attribute(name: str, data: dict) -> str:
        if name in data:
            return data[name]
        return None

    @staticmethod
    def __convert_text_to_date(date_txt: str) -> datetime.datetime:
        date_components = date_txt.split("-")
        return datetime.datetime(
            year=int(date_components[0]),
            month=int(date_components[1]),
            day=int(date_components[2])
        )

    def age_as_range(self):
        if self.edad == "ADULTO MAYOR":
            return "65+"
        elif self.edad == "MAYOR DE EDAD":
            return "18-65"
        elif self.edad == "MENOR DE EDAD":
            return "0-18"
        else:
            return "NON-VALID"


class Delitos:

    def __init__(self, raw_csv_data: List[Dict]):
        self.delitos: List[Delito] = []
        self.__parse_raw_data(raw_csv_data)

    def dummy(self):
        pass

    def __parse_raw_data(self, raw_data):
        for delito_dict in raw_data:
            self.delitos.append(Delito(data=delito_dict))

    def count_delitos_in_province(self, province: str):
        count: int = 0
        for delito in self.delitos:
            if delito.provincia == province.upper():
                count = count + 1
        return count

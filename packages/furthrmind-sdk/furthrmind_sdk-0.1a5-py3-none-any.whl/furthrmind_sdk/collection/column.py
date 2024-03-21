from typing_extensions import Self, List, Dict

from ..utils import furthr_wrap
from furthrmind_sdk.collection.baseclass import BaseClass
from furthrmind_sdk.collection.fielddata import FieldData


class Column(BaseClass):
    id = ""
    name = ""
    type = ""
    values = []


    _attr_definition = {
        "columns": {"class": "Column"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def get_all(cls, project_id=None) -> List[Self]:
        raise ValueError("Not implemented for datatables")

    def _get_url(self, id=None, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        if id is None:
            url = f"{project_url}/column/{self.id}"
        else:
            url = f"{project_url}/column/{id}"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/column"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/column"
        return url

    @classmethod
    def _type_check(cls, column_type, data):
        if not column_type in ["Text", "Numeric"]:
            raise ValueError("Column type must be Text/Numeric")

        if column_type == "Text":
            if all([isinstance(d, str) for d in data]):
                return data
            return [str(d) for d in data]

        elif column_type == "Numeric":
            if all([isinstance(d, (int, float)) for d in data]):
                return data
            new_data = []
            for d in data:
                try:
                    new_data.append(float(d))
                except:
                    raise ValueError("All column values must be a float, int or a string that can be converted to a float")
            return new_data

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name: str, type: str, data: list, unit=None, project_id=None) -> Self:
        """
        Method to create a new data column
        :param name: Name of the column
        :param type: Type of the column, Either "Text" or "Numeric". Data must fit to type, for Text all data
                            will be converted to string and for Numeric all data is converted to float (if possible)
            :param data: List of column values, must fit to column_type
            :param unit: dict with id or name, or name as string, or id as string
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return: Instance of column class
        """

        data = cls._type_check(type, data)
        unit = FieldData._check_unit(unit)
        data_dict = {"name": name, "type": type, "values": data, "unit": unit}
        id = cls.post(data_dict, project_id)
        data_dict["id"] = id
        return data_dict

    @classmethod
    @BaseClass._create_instances_decorator
    def create_many(cls, data_list: List[Dict], project_id=None) -> Self:
        """
        Method to create a new data column
        :param data_list: dict with the following keys:
            - name: Name of the column
            - type: Type of the column, Either "Text" or "Numeric". Data must fit to type, for Text all data
                    will be converted to string and for Numeric all data is converted to float (if possible)
            - data: List of column values, must fit to column_type
            - unit: dict with id or name, or name as string, or id as string
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return: List with instances of column class
        """

        new_data_list = []
        for item in data_list:
            type = item.get("type")
            unit = item.get("unit")
            name = item.get("name")
            data = item.get("data")
            data = cls._type_check(type, data)
            unit = FieldData._check_unit(unit)
            data_dict = {"name": name, "type": type, "values": data, "unit": unit}
            new_data_list.append(data_dict)

        id_list = cls.post(new_data_list, project_id)
        for item, id in zip(new_data_list, id_list):
            item["id"] = id

        return new_data_list
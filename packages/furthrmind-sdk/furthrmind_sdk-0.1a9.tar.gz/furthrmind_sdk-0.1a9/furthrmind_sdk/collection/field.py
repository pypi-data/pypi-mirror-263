from furthrmind_sdk.collection.baseclass import BaseClass
from typing_extensions import List, Self, Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from furthrmind_sdk.collection.comboboxentry import ComboBoxEntry

class Field(BaseClass):
    id = ""
    name = ""
    type = ""
    script = ""
    comboboxentries: List["ComboBoxEntry"] = []

    _attr_definition = {
        "comboboxentries": {"class": "ComboBoxEntry"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url_instance(self, project_id=None):
        project_url = Field.fm.get_project_url(project_id)
        url = f"{project_url}/fields/{self.id}"
        return url

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields"
        return url

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name, type, project_id=None) -> Self:
        """
        Method to create a new sample

        :param name: the name of the field to be created
        :param type: field type of the field. Must be out of:
            - Numeric
            - Date
            - SingleLine
            - ComboBoxEntry
            - MultiLine
            - CheckBox
            - Calculation

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return instance of the sample class

        """

        if not name:
            raise ValueError("Name cannot be empty")

        if not type ["Numeric", "Date", "SingleLine", "ComboBoxEntry", "MultiLine", "CheckBox", "Calculation"]:
            raise ValueError("type must be one of Numeric, Date, SingleLine, ComboBoxEntry, MultiLine, CheckBox, Calculation")

        data = {"name": name, "type": type}
        id = cls.post(data, project_id)
        data["id"] = id
        return data

    @classmethod
    @BaseClass._create_instances_decorator
    def create_many(cls, data_list: List[Dict], project_id=None) -> Self:
        """
        Method to create multiple samples

        :param data_list: dict with the following keys:
        - name: the name of the field to be created
        - type: field type of the field. Must be out of:
            - Numeric
            - Date
            - SingleLine
            - ComboBoxEntry
            - MultiLine
            - CheckBox
            - Calculation

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return list with instance of the sample class
        """

        for data in data_list:
            if not "name" in data:
                raise ValueError("Name cannot be empty")

            if not data.get("type") in ["Numeric", "Date", "SingleLine", "ComboBoxEntry", "MultiLine", "CheckBox", "Calculation"]:
                raise ValueError(
                    "type must be one of Numeric, Date, SingleLine, ComboBoxEntry, MultiLine, CheckBox, Calculation")

        id_list = cls.post(data_list, project_id)
        for data, id in zip(data_list, id_list):
            data["id"] = id
        return data_list

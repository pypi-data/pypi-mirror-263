from ..utils import furthr_wrap
from furthrmind_sdk.collection.baseclass import BaseClass
from typing_extensions import Self, List, TYPE_CHECKING
if TYPE_CHECKING:
    from furthrmind_sdk.collection import Column

class DataTable(BaseClass):
    id = ""
    name = ""
    columns = []


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
            url = f"{project_url}/rawdata/{self.id}"
        else:
            url = f"{project_url}/rawdata/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/rawdata"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/rawdata"
        return url

    def get_columns(self, column_id_list: List[str]=None, column_name_list:List[str]=None) -> List["Column"]:
        columns = self._get_columns(column_id_list, column_name_list)
        new_column_mapping = {c.id: c for c in columns}
        new_column_list = []
        for column in self.columns:
            if column.id in new_column_mapping:
                new_column_list.append(new_column_mapping[column.id])
            else:
                new_column_list.append(column)
        self.columns = new_column_list
        return columns


    @BaseClass._create_instances_decorator
    @furthr_wrap(force_list=True)
    def _get_columns(self, column_id_list: List[str]=None, column_name_list:List[str]=None) -> List["Column"]:
        if column_id_list:
            pass
        elif column_name_list:
            column_id_list = []
            for column in self.columns:
                if column.name in column_name_list:
                    column_id_list.append(column.id)
        else:
            column_id_list = [c.id for c in self.columns]

        column_id_string = ",".join(column_id_list)
        project_url = self.fm.get_project_url()
        url = f"{project_url}/columns/{column_id_string}"
        columns = self.fm.get(url)
        return columns

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name: str = "Data table", experiment_id=None, sample_id=None, researchitem_id=None, columns=None, project_id=None) -> Self:
        """
        Method to create a new datatable
        :param name: name of the datatable
        :param experiment_id: id of the experiment where the datatable belongs to
        :param sample_id: id of the sample where the datatable belongs to
        :param researchitem_id: id of the researchitem where the datatable belongs to
        :param columns: a list of columns that should be added to the datatable. List with dicts with the following keys:
            - name: name of the column
            - type: Type of the column, Either "Text" or "Numeric". Data must fit to type, for Text all data
                    will be converted to string and for Numeric all data is converted to float (if possible)
            - data: List of column values, must fit to column_type
            - unit: dict with id or name, or name as string, or id as string
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return: instance of datatable class
        """
        from furthrmind_sdk.collection import Column

        if not name:
            raise ValueError("Name must be specified")

        if not experiment_id and not sample_id and not researchitem_id:
            raise ValueError("Either experiment_id or sample_id or researchitem_id must be specified")

        column_id_list = []
        if columns:
            columns = Column.create_many(columns)
            column_id_list = [c.id for c in columns]

        data = {"name": name}
        if column_id_list:
            data["columns"] = [{"id": column_id} for column_id in column_id_list]

        if experiment_id:
            data["experiment"] = {"id": experiment_id}

        if sample_id:
            data["sample"] = {"id": sample_id}

        if researchitem_id:
            data["researchitem"] = {"id":researchitem_id}

        id = cls.post(data, project_id)
        data["id"] = id
        return data


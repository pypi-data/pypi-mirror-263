from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClass

class Category(BaseClass):
    id = ""
    name = ""
    description = ""
    project = ""

    _attr_definition = {
        "project": {"class": "Project"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)


    def _get_url(self, id=None, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        if id is None:
            url = f"{project_url}/researchcategory/{self.id}"
        else:
            url = f"{project_url}/researchcategory/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory"
        return url

    @staticmethod
    def create():
        pass





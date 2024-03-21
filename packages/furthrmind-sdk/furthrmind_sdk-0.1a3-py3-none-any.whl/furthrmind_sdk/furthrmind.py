import requests
from furthrmind_sdk.collection.project import Project

class FURTHRmind:

    def __init__(self, host, api_key, project_id=None, project_name=None):

        if not host.startswith("http"):
            host = f"https://{host}"
        self.host = host
        self.base_url = f"{host}/api2"
        self.session = requests.session()
        self.session.headers.update({"X-API-KEY": api_key})
        self.api_key = api_key
        self.project_id = project_id
        self._write_fm_to_base_class()

        if project_name is not None:
            projects = Project.get_all()
            for project in projects:
                if project["name"].lower() == project_name.lower():
                    self.project_id = project["id"]
                    print(f"Project ID: {self.project_id}")
                    break
        self.project_url = f"{self.base_url}/projects/{self.project_id}"


    def get_project_url(self, project_id=None):
        if project_id is None:
            return self.project_url
        else:
            project_url = self.project_url.replace(self.project_id, project_id)
            return project_url

    def get_projects(self):
        return self.get.project()

    def _write_fm_to_base_class(self):
        from furthrmind_sdk.collection.baseclass import BaseClass
        BaseClass.fm = self




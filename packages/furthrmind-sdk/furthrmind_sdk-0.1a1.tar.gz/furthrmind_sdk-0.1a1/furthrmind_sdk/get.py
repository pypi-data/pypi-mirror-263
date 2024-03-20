from utils import furthr_wrap
from furthrmind_sdk.collection.experiment import Experiment

class Get:
    def __init__(self, fm):
        self.fm = fm

    @furthr_wrap
    def project(self, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        return self.fm.session.get(project_url)

    @furthr_wrap
    def projects(self):
        return self.fm.session.get(f"{self.fm.base_url}/projects")

    @furthr_wrap
    def group(self, group_id, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        url = f"{project_url}/groups/{group_id}"
        return self.fm.session.get(url)

    @furthr_wrap
    def groups(self, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        url = f"{project_url}/groups"
        return self.fm.session.get(url)

    @furthr_wrap
    def experiment(self, exp_id, project_id=None):
        exp = Experiment(self.fm, exp_id)
        return exp.get(exp_id, project_id)

    @furthr_wrap
    def experiments(self, project_id=None):
        exp = Experiment(self.fm)
        return exp.get_all(project_id)

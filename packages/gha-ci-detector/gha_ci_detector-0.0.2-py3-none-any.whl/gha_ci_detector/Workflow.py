import gha_ci_detector.util as util
from gha_ci_detector.Job import Job


class Workflow:
    def __init__(self, file_content: str, name: str = ""):
        self.file_content: str = file_content
        self.yaml: dict = util.parse_yaml(file_content)
        self.name = name
        self.smells = set()

    @classmethod
    def from_file(cls, filepath):
        data = open(filepath).read()
        return cls(data, filepath)

    def get_jobs(self) -> list[Job]:
        jobs = self.yaml['jobs']
        return list(map(lambda x: Job(x, self.yaml['jobs'][x]), jobs))

    def get_keys(self) -> list[str]:
        return list(self.yaml.keys())

    def get_on(self) -> dict | None:
        if 'on' in self.yaml.keys():
            return self.yaml["on"]
        else:
            return None

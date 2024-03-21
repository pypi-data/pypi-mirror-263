class Step:
    def __init__(self, yaml):
        self.yaml: dict = yaml

    def get_if(self) -> str | None:
        if "if" in self.yaml.keys():
            return self.yaml["if"]
        else:
            return None

    def get_name(self) -> str | None:
        if "name" in self.yaml.keys():
            return self.yaml["name"]
        else:
            return None

    def get_uses(self) -> str | None:
        if "uses" in self.yaml.keys():
            return self.yaml["uses"]
        else:
            return None

    def __eq__(self, other):
        if not isinstance(other, Step):
            return False
        if "uses" in self.yaml.keys() and "uses" in other.yaml.keys():
            return self.yaml["uses"] == other.yaml["uses"]
        elif "run" in self.yaml.keys() and "run" in self.yaml.keys():
            return self.yaml["run"] == other.yaml["run"]
        else:
            return False

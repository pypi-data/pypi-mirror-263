import io

from ruamel.yaml import YAML


def parse_yaml(yaml_str: str | None) -> dict | None:
    if yaml_str is None:
        return None
    yaml = YAML()
    try:
        content = yaml.load(io.StringIO(yaml_str))
        return content
    except Exception:
        print("Unable to parse yaml file: " + yaml_str)
        return None


def print_smells(smells: set) -> None:
    print(f"We have found {len(smells)} smells")
    for s in smells:
        print("\t- " + s)


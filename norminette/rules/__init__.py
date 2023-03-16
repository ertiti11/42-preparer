import importlib
import os
from glob import glob

from .rule import PrimaryRule
from .rule import Rule


path = os.path.dirname(os.path.realpath(__file__))

files = glob(path + "/check_*.py")

print("\n\n\n\n\n\n\n")

rules = {}
primary_rules = {}

for f in files:
    mod_name = f.split(os.path.sep)[-1].split(".")[0] #check_assignation
    print(mod_name + "\n\n\n")
    class_name = "".join([s.capitalize() for s in mod_name.split("_")])
    print(class_name)
    module = importlib.import_module(".rules." + mod_name)
    rule = getattr(module, class_name)
    rule = rule()
    rules[class_name] = rule

# files = glob(path + "/is_*.py")

# for f in files:
#     mod_name = f.split(os.path.sep)[-1].split(".")[0]
#     class_name = "".join([s.capitalize() for s in mod_name.split("_")])
#     module = importlib.import_module("rules." + mod_name)
#     rule = getattr(module, class_name)
#     primary_rules[class_name] = rule()


# primary_rules = [v for k, v in sorted(primary_rules.items(), key=lambda item: -item[1].priority)]
# __all__ = ["rules", "primary_rules"]

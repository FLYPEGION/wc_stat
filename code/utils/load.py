import os
import yaml

def load_config(configFile):
    with open(os.path.join(__file__, os.pardir, os.pardir, configFile),'rb') as f:
        configs = yaml.safe_load(f)
    return configs
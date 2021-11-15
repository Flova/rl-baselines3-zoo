#!/usr/bin/python3

import os
import yaml
import sys

print("Usage: First arg is the log folder e.g. 'logs/ppo/', the second one is name of the expriment config file, which is declared by setting the env_kwarg 'config_file'.")

experiments = {}
for folder in os.listdir(str(sys.argv[1])):
    print(folder)
    args_file = os.path.join(str(sys.argv[1]), folder, "soccer_world-v0/args.yml")
    try:
        with open(args_file, "r") as f:
            data = yaml.load(f, Loader=yaml.Loader)
        cfg = data["env_kwargs"]["config_file"]
        experiments[folder] = cfg
    except FileNotFoundError:
        print("Incomplete log")
    print("--------------------------")


def fetch_experiments(name):
    return list(filter(lambda x: x[1]==f"{name}.yaml", experiments.items()))

def fetch_newest_experiment(name):
    return max(fetch_experiments(name), key=lambda x: int(x[0].split("_")[-1]))

if __name__ == "__main__":
    experiment_name = str(sys.argv[2])
    print("\n\nAll experiments with this configuration:")
    print(fetch_experiments(experiment_name))
    print("\n\nNewest experiment:")
    print(fetch_newest_experiment(experiment_name))

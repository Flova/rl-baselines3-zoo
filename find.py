#!/usr/bin/python3

import os
import yaml
import sys

print("Usage: First arg is the log folder e.g. 'logs/ppo/', the second one is name of the expriment config file, which is declared by setting the env_kwarg 'config_file'.")

class Finder:
    def __init__(self, path, verbose):
        self.verbose = verbose
        # Parse logs
        self.experiments = {}
        for folder in os.listdir(path):
            if verbose: print(folder)
            args_file = os.path.join(path, folder, "soccer_world-v0/args.yml")
            try:
                with open(args_file, "r") as f:
                    data = yaml.load(f, Loader=yaml.Loader)
                cfg = data["env_kwargs"]["config_file"]
                self.experiments[folder] = cfg
            except FileNotFoundError:
                if verbose:
                    print("Incomplete log")
            if verbose: print("--------------------------")
        if verbose: print("\n\n")

    def fetch_experiments(self, name):
        return list(filter(lambda x: x[1]==f"{name}.yaml", self.experiments.items()))

    def fetch_newest_experiment(self, name):
        return max(self.fetch_experiments(name), key=self._rank_from_key)

    def format_result(self, result):
        return " -> ".join(result)

    def format_results(self, results):
        return '\n'.join(map(self.format_result, sorted(results, key=self._rank_from_key)))

    def _rank_from_key(self, name):
        return int(name[0].split("_")[-1]) 


if __name__ == "__main__":
    f = Finder(str(sys.argv[1]), verbose=False)
    experiment_name = str(sys.argv[2])
    print(f"""
All experiments with this configuration:
{f.format_results(f.fetch_experiments(experiment_name))}

Newest experiment:
{f.format_result(f.fetch_newest_experiment(experiment_name))}""")

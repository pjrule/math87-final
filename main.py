import argparse
import json
from scenario import Scenario, ViewingMode

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--config', type=str,
                        help='Configuration file',
                        default='config.json')
    args = parser.parse_args()
    with open(args.config, 'r') as infile:
        config = json.load(infile)
        print(config)
        num_simulations = config['num_simulations']
        turns_per_simulation = config['turns_per_simulation']
        

from collections import defaultdict
from tqdm import tqdm
import json

from genomes import get_genomes
from targets import get_targets

genomes = get_genomes()

target_sources = defaultdict(list)

for genome in tqdm(genomes.keys()):
    targets = get_targets(genome)
    for target in targets:
        # Transform first letter to lower case
        target_lower = target[0].lower() + target[1:]
        target_sources[target_lower].append(genome)

with open("sources.json", "w") as f:
    json.dump(target_sources, f, indent=2)

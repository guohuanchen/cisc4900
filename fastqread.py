import sys
import os
#from collections import Counter

def process(lines=None):
    ks = ['sequence_identifier', 'sequence', 'quality_score_identifier', 'quality_score']
    return {k: v for k, v in zip(ks, lines)}

try:
    fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

n = 4
with open(fn, 'r') as fh:
    lines = []
    for line in fh:
        lines.append(line.rstrip())
        if len(lines) == n:
            record = process(lines)
            sys.stderr.write("RecordL: %s\n" % (str(record)))
            lines = []

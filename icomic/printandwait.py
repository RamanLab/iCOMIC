import sys
import subprocess

subprocess.Popen(["snakemake", "--use-conda"], shell=True, stdout= subprocess.PIPE)

sys.stdout.flush()



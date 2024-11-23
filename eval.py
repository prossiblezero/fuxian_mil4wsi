import submitit,sys,os
from utilsmil4wsi.process import eval
os.environ["WANDB__SERVICE_WAIT"] = "300"

from utilsmil4wsi.parser import get_args
from utilsmil4wsi.experiments import *
from utilsmil4wsi.process import processDataset
# Ensure that all operations are deterministic on GPU (if used) for reproducibility

def main():
    args = get_args()
    executor = submitit.AutoExecutor(folder=args.logfolder, slurm_max_num_timeout=30)
    executor.update_parameters(
            mem_gb=args.mem,
            slurm_gpus_per_task=args.nodes,
            tasks_per_node=args.nodes,  # one task per GPU
            slurm_cpus_per_gpu=args.nodes,
            nodes=args.nodes,
            timeout_min=args.time,  # max is 60 * 72
            # Below are cluster dependent parameters
            slurm_partition=args.partition,
            slurm_signal_delay_s=120,
            slurm_array_parallelism=args.job_parallel)
    executor.update_parameters(name=args.job_name)
    experiments=[]
    if args.dataset== "cam":
        experiments=experiments+launch_DASMIL_cam(args)
    else:
        experiments=experiments+launch_DASMIL_lung(args)
    executor.map_array(eval,experiments)
    #eval(experiments[1])

if __name__ == '__main__':
    main()

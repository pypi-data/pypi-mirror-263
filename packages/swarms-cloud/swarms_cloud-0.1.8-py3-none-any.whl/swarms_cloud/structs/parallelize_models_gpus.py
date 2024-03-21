import os
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup_distributed_environment():
    """Set up the distributed environment variables."""
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    # Ensure these are properly configured or dynamically set in a real-world scenario

def initialize_process_group(backend='nccl'):
    """Initialize the distributed environment."""
    dist.init_process_group(backend)

def prepare_model_for_ddp_inference(model):
    """Prepare and wrap the model for DDP execution in inference mode, considering bitsandbytes models."""
    
    model.eval()  # Ensure the model is in eval mode regardless of its type
    
    if torch.cuda.is_available() and torch.cuda.device_count() > 1:
        setup_distributed_environment()
        initialize_process_group()
        
        rank = dist.get_rank()
        world_size = dist.get_world_size()
        
        print(f"Rank {rank}/{world_size} - Preparing model for DDP inference")
        
        # When using DDP for inference, ensure you're not backpropagating through the model
        model = DDP(model, device_ids=[rank], output_device=rank, find_unused_parameters=False)
    else:
        print("Single GPU/CPU detected. Proceeding without DDP.")
    
    return model

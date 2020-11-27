import os
import numpy as np

if __name__ == "__main__":
    
    learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]

    print(learning_rates)
    # batch_sizes = [1,5,10,20]


    for lr in learning_rates:
        command = f"python pytorch_mlp_framework/train_evaluate_image_classification_system.py --batch_size 100 --seed 0 --num_filters 32 --num_stages 3 --num_blocks_per_stage 5 --experiment_name master_experiments/lr{lr} --use_gpu True --num_classes 100 --block_type 'conv_block_bn' --continue_from_epoch -1 --learning_rate {lr}"
        #python pytorch_mlp_framework/train_evaluate_image_classification_system.py --batch_size 100 --seed 0 --num_filters 32 --num_stages 3 --num_blocks_per_stage 0 --experiment_name VGG_08_bn_experiment --use_gpu True --num_classes 100 --block_type 'conv_block_bn' --continue_from_epoch -1

        os.system(command)
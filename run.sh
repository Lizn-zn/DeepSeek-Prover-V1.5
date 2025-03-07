# CUDA_VISIBLE_DEVICES=4 python quick_start.py

# CUDA_VISIBLE_DEVICES=4 python -m prover.launch --config=configs/sampling.py --log_dir=logs/RMaxTS_results

CUDA_VISIBLE_DEVICES=4 python -m prover.summarize --config=configs/RMaxTS.py --log_dir=logs/RMaxTS_results
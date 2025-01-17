import torch
from audioldm_eval import EvaluationHelper

# device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'

generation_result_path = "example/paired"
# generation_result_path = "example/unpaired"
target_audio_path = "example/reference"

evaluator = EvaluationHelper(16000, device)

# Perform evaluation, result will be print out and saved as json
metrics = evaluator.main(
    generation_result_path,
    target_audio_path,
)
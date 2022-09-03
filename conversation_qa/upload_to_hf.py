import os
import torch

from transformers import GPT2Tokenizer, GPT2LMHeadModel

_path = os.path.dirname(__file__)
_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
_model = GPT2LMHeadModel.from_pretrained("gpt2")
checkpoint = torch.load(
    os.path.join(_path, "../models/save_small6"), map_location="cpu"
)
_model.load_state_dict(checkpoint["model_state_dict"])

if __name__ == "__main__":
    print("Uploading to HF")
    _model.push_to_hub("conversation-qa")
    _tokenizer.push_to_hub("conversation-qa")

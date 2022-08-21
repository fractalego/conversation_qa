import torch

_device = "cuda" if torch.cuda.is_available() else "cpu"


def get_answer_prompt(story, dialogue, query):
    return f"""
In the text below two people are discussing a story.

Story:
{story}

Discussion:
{dialogue}
Q: {query}
A: 
""".strip()


def generate_answer(model, tokenizer, prompt, length=5):
    model.eval()
    with torch.no_grad():
        tokens = tokenizer.encode(prompt, return_tensors="pt")
        text = prompt
        start = len(prompt)
        while "\n" not in text[start:]:
            output = _inference(model, tokenizer, tokens.to(_device), length)
            decoded = tokenizer.decode(output[0], skip_special_tokens=True)
            text += decoded[len(text) :]
            tokens = output

    end = text.find("\n", start)
    return text[start:end].split(":")[-1].strip()


def _inference(model, tokenizer, tokens, length):
    return model.generate(
        tokens.to(_device),
        max_length=tokens.shape[1] + length,
        pad_token_id=tokenizer.eos_token_id,
    )

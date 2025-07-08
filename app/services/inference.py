from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load model on CPU
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,  # Use float32 to avoid issues
    device_map=None  # Explicitly avoid GPU
)

# Set model to eval mode
model.eval()

# Inference function
async def get_chat_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):].strip()

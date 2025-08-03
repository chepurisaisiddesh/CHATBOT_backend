# src/model.py
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
import torch

model_name = "MBZUAI/LaMini-Flan-T5-783M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    trust_remote_code=True
)

text_gen_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1,  # -1 = CPU
    max_length=1024,
    do_sample=True,
    top_p=0.95,
    temperature=0.8,
)

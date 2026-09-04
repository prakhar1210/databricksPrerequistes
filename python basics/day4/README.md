# Day 4 - LLM and Prompt Engineering Basics

This folder contains Day 4 practice for the Databricks Gen AI Associate certification. The focus is on understanding large language models and writing prompts that guide them toward useful, grounded, and structured responses.

## Files

### `exer1.py`

This file contains four prompt-building exercises.

#### Exercise 1: Basic Prompt

`create_prompt(question)` builds a prompt that gives the model a role, asks for a clear answer, and inserts the user's question.

#### Exercise 2: RAG Prompt

`create_rag_prompt(question, context)` instructs the model to answer using only supplied context. It also tells the model to say when the context does not contain enough information. This pattern can help reduce hallucinations.

#### Exercise 3: Few-Shot Classification

`few_shot_prompt(review)` includes positive and negative review examples before asking the model to classify a new review. These examples demonstrate the expected task and output format.

#### Exercise 4: Structured Information Extraction

`extract_candidate_info(resume)` asks the model to extract a candidate's name, skills, experience, and current role. It requests that the response contain only valid JSON.

## Concepts Practiced

- Prompt roles and clear instructions
- Context-grounded answers
- Retrieval-Augmented Generation (RAG)
- Few-shot prompting
- Sentiment classification
- Structured output using JSON
- Prompt templates with dynamic questions and context
- Reducing unsupported answers by limiting the information source

## Key LLM Topics

- An LLM is a large language model trained to understand and generate text.
- Training teaches a model patterns from data; inference is when the trained model generates an answer.
- A token is a unit of text processed by a model. Tokens may be words, parts of words, punctuation, or spaces.
- Tokens matter because context windows, costs, and output limits are measured in tokens.
- A context window is the maximum amount of input and output token information a model can handle in one request.
- Prompt engineering is the practice of designing clear instructions, context, examples, and output requirements.
- Zero-shot prompting gives a task without examples; few-shot prompting provides examples to demonstrate the desired behavior.
- System instructions define high-level behavior and rules; user instructions provide the specific request.
- Prompt injection is an attempt to manipulate a model into ignoring its intended instructions or revealing information it should not expose.
- Hallucination occurs when a model generates information that sounds plausible but is unsupported or incorrect.
- Temperature controls randomness. Lower values usually produce more predictable responses, while higher values allow more variation.
- `max_tokens` limits the maximum number of tokens generated in the response.
- Structured output follows a defined format, such as JSON, so the result can be processed reliably by software.

## Why Prompt Templates Are Useful

Prompt templates provide a repeatable structure while allowing values such as questions, documents, or user details to change. They make prompts easier to test, maintain, and reuse in applications.

## Why Large Documents Cannot Simply Be Sent to an LLM

A large document may exceed the model's context window. Sending unnecessary text also increases token cost, processing time, and the chance that important information is overlooked. Large documents should be split into smaller chunks and the most relevant chunks selected for the question.

## How RAG Helps Reduce Hallucinations

RAG retrieves relevant information from a trusted data source and supplies it as context to the LLM. The model can then generate an answer grounded in that retrieved content instead of relying only on its general training. A good RAG system should still validate sources, retrieve relevant chunks, and instruct the model not to invent information that is missing.

## Running the Exercise

From the Day 4 folder, run:

```powershell
C:/Python311/python.exe exer1.py
```

The script prints the four generated prompts for inspection. It does not call an external LLM API; it only prepares prompt text.

## Next Steps

- Compare zero-shot and few-shot results with real model calls.
- Add input validation for structured JSON output.
- Experiment with prompt wording and output constraints.
- Build a simple chunking and retrieval workflow for RAG.

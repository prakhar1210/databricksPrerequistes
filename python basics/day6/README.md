# RAG File Demo

This example demonstrates the basic retrieval stage of a Retrieval-Augmented Generation (RAG) workflow using a small in-memory employee-policy knowledge base.

## What It Demonstrates

- Storing documents as dictionaries with IDs and text
- Searching documents using words from a user query
- Ranking documents by the number of matching words
- Selecting the top relevant documents
- Building a context string for a later generation step

## How It Works

The `retrieve_documents()` function compares each query word with each document's text. Every matching word increases that document's score. Results are then sorted from the highest score to the lowest score.

The `create_context()` function takes the top results and joins their text into one context string. In a complete RAG application, this context would be passed to a language model along with the user's question.

## Run the Example

From the repository root, run:

```powershell
python "python basics/day6/ragfile.py"
```

The script prints the score and text for each retrieved document, followed by the top-two context documents.

## Notes

This is a simple learning example rather than a production retrieval system. It uses keyword matching instead of embeddings or a vector database, so it does not understand synonyms or semantic similarity.
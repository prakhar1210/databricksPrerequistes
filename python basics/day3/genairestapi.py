documents = [
    {
        "id": 1,
        "title": "Databricks",
        "content": "Databricks is a unified data and AI platform."
    },
    {
        "id": 2,
        "title": "RAG",
        "content": "RAG retrieves relevant documents and provides them to an LLM."
    },
    {
        "id": 3,
        "title": "MLflow",
        "content": "MLflow helps manage machine learning and generative AI applications."
    }
]


def search_documents(query, documents):
    results = []
    for document in documents:
        if query.lower() in document["title"].lower() or query.lower() in document["content"].lower():
            results.append(document)
    return results


results = search_documents("RAG", documents)
print("Search results:")
for result in results:
    print(result)

# knowledge base:

documents = [
    {
        "id": 1,
        "text": "Employees receive 24 paid leave days per year."
    },
    {
        "id": 2,
        "text": "Employees receive health insurance coverage."
    },
    {
        "id": 3,
        "text": "Employees can work remotely three days per week."
    },
    {
        "id": 4,
        "text": "Employees receive a company laptop."
    }
]


# simple retrieval function to search for relevant documents based on a query
def retrieve_documents(query, documents):

    results = []

    query_words = query.lower().split()

    for document in documents:

        text = document["text"].lower()

        score = 0

        for word in query_words:

            if word in text:
                score += 1

        results.append(
            {
                "document": document,
                "score": score
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# test the retrieval function with a sample query
query = "How many paid leaves do employees receive?"

results = retrieve_documents(
    query,
    documents
)

for result in results:
    print(
        result["score"],
        result["document"]["text"]
    )


# create a context string from the top-k relevant documents

def create_context(results, top_k=2):

    selected = results[:top_k]

    context = "\n".join(
        result["document"]["text"]
        for result in selected
    )

    return context


context = create_context(results, top_k=2)

print(context)
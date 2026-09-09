import math


def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))

    magnitude_v1 = math.sqrt(sum(a * a for a in v1))
    magnitude_v2 = math.sqrt(sum(b * b for b in v2))

    return dot_product / (magnitude_v1 * magnitude_v2)


def search_documents(question_vector, embeddings, top_k=2):

    results = []

    for doc_id, vector in embeddings.items():

        similarity = cosine_similarity(
            question_vector,
            vector
        )

        results.append(
            (doc_id, similarity)
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results[:top_k]


# Document embeddings
embeddings = {
    "doc1": [0.9, 0.1, 0.2],
    "doc2": [0.1, 0.8, 0.2],
    "doc3": [0.7, 0.2, 0.3],
    "doc4": [0.2, 0.1, 0.9]
}

# Query/question embedding
question_vector = [0.8, 0.2, 0.3]

# Search
results = search_documents(
    question_vector,
    embeddings,
    top_k=2
)

print(results)
from sentence_transformers import SentenceTransformer
from app.database.chroma_client import get_collection

MODEL_NAME = "all-MiniLM-L6-v2"

def main():

    model = SentenceTransformer(MODEL_NAME)

    collection = get_collection()

    print("\nAnime Retrieval Test")
    print("--------------------")

    while True:

        query = input("\nQuery (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        query_embedding = model.encode(
            query,
            normalize_embeddings=True,
        )

        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=10,
        )

        print("\nTop Recommendations\n")

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for i, (doc, meta, distance) in enumerate(
            zip(documents, metadatas, distances),
            start=1,
        ):

            similarity = 1 - distance

            print(f"{i}. {doc}")
            print(f"   Genre : {meta['genre']}")
            print(f"   Score : {meta['score']}")
            print(f"   Studio: {meta.get('studio', 'Unknown')}")
            print(f"   Similarity: {similarity:.3f}")
            print()


if __name__ == "__main__":
    main()
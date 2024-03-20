# import llama_index.core
from datasets import Dataset


def retriever_test(
    client, collection: str, dataset: Dataset, embed_model
) -> dict:
    embed_results = embed_model.embed(
        texts=dataset["question"],
        model="embed-english-v3.0",
        input_type="search_query",
    )

    chunk_ids_response = []
    for idx, val in enumerate(dataset):
        # source_nodes = retriever.retrieve(set['question'])
        response = client.search(
            collection_name=collection,
            query_vector=embed_results.embeddings[idx],
            limit=3,
        )
        id_list = [x.id for x in response]
        if val["chunk_id"] in id_list:
            chunk_ids_response.append(True)
        else:
            chunk_ids_response.append(False)

    acc = len([x for x in chunk_ids_response if x]) / len(chunk_ids_response)
    return {"Accuracy": acc}

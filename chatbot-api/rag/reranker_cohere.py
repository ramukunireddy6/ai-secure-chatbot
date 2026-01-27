import cohere
import os

co = cohere.Client(os.environ["COHERE_API_KEY"])
def rerank(query:str, documents:list[str], top_k:int=3):
    """
    uses cohere rerank to reorder retrieved documents
    :param query:
    :param document:
    :param top_k:
    :return:
    """
    if not documents:
        return []

    response=co.rerank(model="rerank-english-3.0",
                       query=query,
                       documents=documents,
                       top_n=top_k
                       )
    return[documents[r.index] for r in response.results]
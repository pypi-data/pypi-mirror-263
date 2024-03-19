from time import time
import numpy as np
from collections import Counter
import openai
from deepllm.params import to_pickle, from_pickle, PARAMS, ensure_openai_api_key, GPT_PARAMS, IS_LOCAL_LLM
import torch
from sentence_transformers import SentenceTransformer
from vecstore.vecstore import VecStore


# SBERT API

def sbert_embed(sents):
    device='cuda' if torch.cuda.is_available() else 'cpu'
    model = SentenceTransformer("all-MiniLM-L6-v2",device=device)
    embeddings = model.encode(sents)
    return embeddings


# LLM API

def llm_embed_old(emebedding_model, sents):
    response = openai.Embedding.create(
        input=sents,
        model=emebedding_model
    )
    embeddings = [response['data'][i]['embedding'] for i in range(len(response['data']))]
    toks = response["usage"]["total_tokens"]
    return np.array(embeddings), toks


def llm_embed_new(emebedding_model, sents):
    CF = PARAMS()

    client = openai.OpenAI(
        api_key=ensure_openai_api_key(),
        base_url=GPT_PARAMS['API_BASE']
    )

    response = client.embeddings.create(
        input=sents,
        model=emebedding_model
    )

    embeddings = [response.data[i].embedding for i in range(len(response.data))]
    toks = response.usage.total_tokens
    return np.array(embeddings), toks


def get_llm_embed_method():
    try:
        if int(openai.__version__[0]) > 0:
            return llm_embed_new
    except Exception:
        pass
    return llm_embed_old


class Embedder:
    """
    embeds a set of sentences using an LLM
    and store them into a vector store
    """

    def __init__(self, cache_name, FORCE_SBERT=True):
        assert cache_name is not None
        self.FORCE_SBERT=FORCE_SBERT
        self.total_toks = 0
        self.cache_name = cache_name
        self.CACHES = None
        self.emebedding_model = None
        self.LOCAL_LLM = IS_LOCAL_LLM[0]
        self.vstore = None
        self.times = Counter()
        PARAMS()(self)

    def cache(self, ending='.pickle'):
        loc = ""
        if self.LOCAL_LLM:
            loc = "_local"

        return self.CACHES + self.cache_name + loc + ending

    def embed(self, sents):
        t1 = time()
        if self.LOCAL_LLM or self.FORCE_SBERT:
            embeddings = sbert_embed(sents)
            kind = 'sbert'
        else:
            llm_embed = get_llm_embed_method()
            embeddings, toks = llm_embed(self.emebedding_model, sents)
            self.total_toks += toks
            kind = 'llm'
        t2 = time()

        self.times[kind + '_embed'] = t2 - t1
        return embeddings

    def get_times(self):
        return self.times | self.vstore.times

    def store(self, sents):
        """
        embeds and caches the sentences and their embeddings
        """
        f = self.cache()
        fb = self.cache(ending='.bin')
        embeddings = self.embed(sents)
        dim = embeddings.shape[1]
        if self.vstore is None:
            self.vstore = VecStore(fb, dim=dim)
        self.vstore.add(embeddings)

        to_pickle((dim, sents), f)
        self.vstore.save()

    def load(self):
        f = self.cache()
        fb = self.cache(ending='.bin')
        dim, sents = from_pickle(f)
        self.vstore = VecStore(fb, dim=dim)
        self.vstore.load()

        return sents

    def query(self, query_sent, top_k):
        """
        fetches the store
        """
        sents = self.load()
        query_embeddings = self.embed([query_sent])
        knn_pairs = self.vstore.query_one(query_embeddings[0], k=top_k)

        answers = [(sents[i], r) for (i, r) in knn_pairs]
        return answers

    def knns(self, top_k):
        assert top_k > 0, top_k
        self.load()
        assert self.vstore is not None
        knn_pairs = self.vstore.all_knns(k=top_k)

        return knn_pairs

    def get_sents(self):
        return from_pickle(self.cache())[1]

    def __call__(self, quest, top_k):
        return self.query(quest, top_k)

    def dollar_cost(self):
        # if self.LOCAL_LLM: return 0.0
        return self.total_toks * 0.0004 / 1000

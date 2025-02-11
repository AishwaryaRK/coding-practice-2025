from collections import defaultdict
from typing import List


class DocumentSearchEngine:
    def __init__(self):
        self.inverted_index = defaultdict(lambda: defaultdict(list))
        self.inverted_index_doc_ids = defaultdict(set)
        self.documents = defaultdict(list)

    def __get_tokens(self, text: str) -> List[str]:
        tokens = text.lower().replace(".", "").split(" ")
        return [token for token in tokens if len(token) > 3]

    def __update_inverted_index(self, doc_id: int, tokens: List[str]):
        for i, token in enumerate(tokens):
            self.inverted_index[token][doc_id].append(i)
            self.inverted_index_doc_ids[token].add(doc_id)

    def __is_phrase_in_doc(self, search_tokens: List[str], doc_id: int) -> bool:
        if len(search_tokens) == 1:
            return True

        first_token = search_tokens[0]
        start_indices = self.inverted_index[first_token][doc_id]
        for start_index in start_indices:
            for i, token in enumerate(search_tokens[1:]):
                index = start_index + i + 1
                if i == len(search_tokens[1:]) - 1 and self.documents[doc_id][index] == token:
                    return True
                if index >= len(self.documents[doc_id]) or (
                        index < len(self.documents[doc_id]) and self.documents[doc_id][index] != token):
                    break
        return False

    def add_doc(self, doc_id: int, text: str):
        tokens = self.__get_tokens(text)
        self.documents[doc_id] = tokens
        self.__update_inverted_index(doc_id, tokens)

    def search(self, phrase: str) -> List[int]:
        search_tokens = self.__get_tokens(phrase)
        doc_ids_per_token = []
        for token in search_tokens:
            doc_ids_per_token.append(self.inverted_index_doc_ids[token])
        doc_ids_intersection = set.intersection(*doc_ids_per_token)
        result = []
        for doc_id in doc_ids_intersection:
            if self.__is_phrase_in_doc(search_tokens, doc_id):
                result.append(doc_id)
        return result


e = DocumentSearchEngine()
e.add_doc(1, "Cloud computing is the on-demand availability of computer system resources.")
e.add_doc(2,
          "One integrated service for metrics uptime cloud monitoring dashboards and alerts reduces time spent navigating between systems.")
e.add_doc(3, "Monitor entire cloud infrastructure, whether in the cloud computing is or in virtualized data centers.")
print(e.search("Cloud computing is"))
print(e.search("cloud monitoring"))
print(e.search("cloud"))

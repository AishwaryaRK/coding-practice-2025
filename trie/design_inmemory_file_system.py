import collections
from typing import List


class FileSystem:
    def __init__(self):
        self.trie = collections.defaultdict(dict)
        self.trie['/'] = {}

    def mkdir(self, path: str):
        path_nodes = path.split('/')
        path_nodes = path_nodes[1:]
        t = self.trie["/"]
        for node in path_nodes:
            if node in t:
                t = t[node]
            else:
                t[node] = {}
                t = t[node]

    def add_content_to_file(self, file_path: str, content: str):
        path_nodes = file_path.split('/')
        path_nodes = path_nodes[1:]
        t = self.trie["/"]
        for i in range(len(path_nodes) - 1):
            node = path_nodes[i]
            if node in t:
                t = t[node]
            else:
                t[node] = {}
                t = t[node]
        if path_nodes[-1] in t and True in t[path_nodes[-1]]:
            t[path_nodes[-1]]["content"] += content
        else:
            t[path_nodes[-1]] = {True: True, "content": content}

    def read_content_from_file(self, file_path: str) -> str:
        path_nodes = file_path.split('/')
        path_nodes = path_nodes[1:]
        t = self.trie["/"]
        for i in range(len(path_nodes) - 1):
            node = path_nodes[i]
            t = t[node]
        return t[path_nodes[-1]]["content"]

    def ls(self, path: str) -> List[str]:
        t = self.trie["/"]
        if path == "/":
            return sorted(list(t.keys()))
        path_nodes = path.split('/')[1:]
        for i in range(len(path_nodes) - 1):
            node = path_nodes[i]
            if node in t:
                t = t[node]
            else:
                t[node] = {}
                t = t[node]
        if True in t:
            return [path_nodes[-1]]
        return sorted(list(t[path_nodes[-1]].keys()))


fs = FileSystem()
print(fs.ls("/"))
print(fs.mkdir("/a/b/c"))
print(fs.add_content_to_file("/a/b/c/d", "hello_d"))
print(fs.ls("/"))
print(fs.read_content_from_file("/a/b/c/d"))
print(fs.add_content_to_file("/a/b/e", "hello_e"))
print(fs.ls("/a/b"))
print(fs.add_content_to_file("/a/b/c/d", "hello_d_again"))
print(fs.read_content_from_file("/a/b/c/d"))


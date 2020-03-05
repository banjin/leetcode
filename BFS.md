广度优先




```python
def BFS(graph, start, end):
    queue = []
    visited = set()
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

        # other processing work

        ...

```


```python

class Solution(object):
    def levelorder(self, root):
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)

        # visited = set(root)

        while queue:
            level_sie = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                currnet_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.addend(node.right)
            result.append(current_level)

        return rusult





```
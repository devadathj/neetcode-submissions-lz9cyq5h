class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        neig = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in neig:
                    neig[pattern] = []
                neig[pattern].append(word)

        output = 1
        q = deque([beginWord])
        visited = {beginWord}

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return output
                
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j + 1:]

                    for k in neig[pattern]:
                        if k not in visited:
                            visited.add(k)
                            q.append(k)
            output += 1

        return 0
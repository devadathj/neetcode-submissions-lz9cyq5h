class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")

        output = []

        for i in path:
            if i:
                if i == "..":
                    if len(output) != 0:
                        output.pop()
                elif i == ".":
                    continue
                else:
                    output.append(i)
        
        return "/" + "/".join(output)
            
            
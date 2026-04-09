class Solution:

    def encode(self, strs: List[str]) -> str:
        
        output = []
        for string in strs:
            for character in string:
                output.append(str(ord(character) + 69) + ",")
            output.append("n,")

        return "".join(output)

    def decode(self, s: str) -> List[str]:

        output = []
        temp_string = []

        for character in s.split(",")[:-1]:
            if character != 'n':
                temp_string.append(chr(int(character) - 69))
            else:
                output.append("".join(temp_string))
                temp_string = []

        return output
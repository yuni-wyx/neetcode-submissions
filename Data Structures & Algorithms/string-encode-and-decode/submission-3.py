class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            length = len(i)
            encoded_string += str(length)
            encoded_string += '@'
            encoded_string += i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = ""
        answer = []
        count = 0
        j = 0
        while count < len(s):
            j = count
            while s[j] != '@':
                j+=1
            length = int(s[count:j])
            start = j+1
            decoded_string = s[start: start+length]
            answer.append(decoded_string)
                
            count = start+length
        
        return answer



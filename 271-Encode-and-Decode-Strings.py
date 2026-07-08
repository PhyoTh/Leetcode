class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for token in strs:
            encoded_str += str(len(token)) + ":/" + token
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        digits = ''
        while i < len(s):
            if s[i].isdigit():
                digits += s[i]
            elif i + 1 < len(s) and s[i] == ':' and s[i + 1] == '/' and digits != '':
                i += 2
                temp = int(digits)
                decoded_str.append(s[i:i+temp])
                digits = ''

                i += temp
                continue
            elif digits != '':
                digits = ''

            i += 1
    
        return decoded_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
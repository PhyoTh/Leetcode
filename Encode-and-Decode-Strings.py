class Codec:
    def encode(self, strs):
        encoded_str = ''
        for s in strs:
            temp = s.replace('/', '//') + '/:'
            encoded_str = encoded_str + temp # join is used to join the list of str with the "-".join, - as dilimeter
        return encoded_str

    def decode(self, s):
        decoded_strs = []
        temp = ''
        i = 0
        while i < len(s): # for loop with range doesn't increment like c++
            if s[i] == '/' and i+1 < len(s) and s[i+1] == '/':
                temp = temp + '/'
                i += 2
            elif s[i] == '/' and i+1 < len(s) and s[i+1] == ':':
                decoded_strs.append(temp)
                temp = ''
                i += 2
            else:
                temp = temp + s[i]
                i += 1
        return decoded_strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
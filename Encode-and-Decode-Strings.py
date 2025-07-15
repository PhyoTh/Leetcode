class Codec:

    def encode(self, strs):
        encoded_string = ''

        for s in strs:
            encoded_string += s.replace('/', '//') + '/:'
        return encoded_string

    def decode(self, s):
        decoded_string = []
        
        current_string = ''
        i = 0
        while i < len(s):
            # for the actual case of splitting
            if s[i: i+2] == '/:':
                decoded_string.append(current_string)
                current_string = ''
                i += 2
            # for the case where we escape
            elif s[i: i+2] == '//':
                current_string += '/'
                i += 2
            else:
                current_string += s[i]
                i += 1
            
        return decoded_string

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
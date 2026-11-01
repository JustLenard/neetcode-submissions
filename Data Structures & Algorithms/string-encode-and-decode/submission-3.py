class Solution:

    def encode(self, strs: List[str]) -> str:
        metadata = '['
        for s in strs:
            metadata += str(len(s)) + ','
        metadata += ']'
        return metadata + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        metadata , encoded_string = s.split(']', maxsplit=1)
        metadata = metadata.replace('[', '').split(',')[:-1]

        decoded_strings = []
        encoded_string = ''.join(encoded_string)
        for m in metadata:
            word = encoded_string[:int(m)]
            decoded_strings.append(word)
            encoded_string = encoded_string[int(m):]
        return decoded_strings 
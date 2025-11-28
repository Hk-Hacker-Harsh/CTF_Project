def transform(input_str):
    xor_key = 0x55 # Hex value for 'U' (85 in decimal)
    xored = "".join([chr(ord(c) ^ xor_key) for c in input_str])
    
    reversed_str = xored[::-1]
    
    final_output = reversed_str.encode().hex()
    
    return final_output


# File: core/cipher_logic.py
# Contains the core mathematical and character shifting logic.

def _shift_char(char, shift, is_encode=True):
    """
    Helper function to apply the shift logic to a single character.
    Handles 'A-Z' and 'a-z' wrap-around.
    """
    
    # 1. Determine the base ASCII value for the current case (A or a)
    if 'a' <= char <= 'z':
        base = ord('a')
    elif 'A' <= char <= 'Z':
        base = ord('A')
    else:
        # Reliability NFR: Preserve non-alphabetic characters
        return char

    # 2. Determine the effective shift direction
    # If decoding, the shift is applied in the opposite direction
    effective_shift = shift if is_encode else -shift

    # 3. Apply the shift using modulo arithmetic for wrap-around
    # char_index = position of char (0-25)
    char_index = ord(char) - base
    
    # new_index = shifted position (0-25), using % 26 for wrap-around
    new_index = (char_index + effective_shift) % 26
    
    # 4. Convert back to the shifted character
    return chr(new_index + base)

def encode_text(text, shift):
    """
    Module I: Encodes text using the Caesar Cipher.
    """
    output = []
    for char in text:
        output.append(_shift_char(char, shift, is_encode=True))
        
    return "".join(output)

def decode_text(text, shift):
    """
    Module II: Decodes text by reversing the Caesar Cipher shift.
    """
    output = []
    # Call _shift_char with is_encode=False to apply the reverse operation
    for char in text:
        output.append(_shift_char(char, shift, is_encode=False))
        
    return "".join(output)

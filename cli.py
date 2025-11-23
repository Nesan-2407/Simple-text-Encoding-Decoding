# File: main_cli.py
# Handles command-line arguments, input validation, and output display.

import argparse
import sys
from core.cipher_logic import encode_text, decode_text

def main():
    """Handles command-line arguments and displays results."""
    parser = argparse.ArgumentParser(
        description="Simple Text Encoder/Decoder (Caesar Cipher).",
        epilog="Use -e to encode, or -d to decode. Requires text and a numeric shift key."
    )
    
    # Mutually exclusive group for the two modes (Usability NFR)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encode', action='store_true', help='Set mode to ENCODE.')
    group.add_argument('-d', '--decode', action='store_true', help='Set mode to DECODE.')
    
    # Required inputs
    parser.add_argument('text', type=str, help='The text to process.')
    parser.add_argument('shift', type=int, help='The integer shift key (e.g., 3).')

    args = parser.parse_args()
    
    try:
        text = args.text
        shift = args.shift
        
        if args.encode:
            result = encode_text(text, shift)
            mode_label = "ENCODED"
        elif args.decode:
            result = decode_text(text, shift)
            mode_label = "DECODED"
        else:
            # Should not be reachable
            return

        # Module III: Output formatting
        print(f"\n--- Caesar Cipher Result ---")
        print(f"Mode: {mode_label}")
        print(f"Shift Key: {shift}")
        print(f"Original Text: {text}")
        print(f"Processed Text: {result}")
        print("----------------------------")

    except TypeError:
        # Reliability NFR: Catch non-integer inputs passed to type=int
        print("Error: The shift key must be a valid integer.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

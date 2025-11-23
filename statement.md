# Simple Text Encoder/Decoder: Project Statement

## Problem Statement
The primary goal is to demonstrate foundational programming principles, specifically related to **string manipulation** and **character encoding**, using a simple, classic cryptographic algorithm (the Caesar Cipher). The project serves as a clear illustration of modular code structure.

## Scope of the Project
The scope is strictly limited to the implementation of the **Caesar Cipher** for encoding and decoding alphabetic characters (A-Z, a-z) using a single integer shift key. It functions as an **interactive Command-Line Interface (CLI)** tool and intentionally avoids external libraries, file I/O, or database integration to maintain simplicity.

## High-Level Features
1.  **Caesar Cipher Logic:** Implements the forward and reverse shift operation.
2.  **Character Set Handling:** Preserves non-alphabetic characters (spaces, numbers, punctuation).
3.  **Input Validation:** Ensures the shift key is a valid integer.

## Modular Structure
The project utilizes a two-layer architecture:
* **Presentation Layer:** Handled by `main_cli.py` (User interaction).
* **Core Logic Layer:** Handled by `core/cipher_logic.py` (Mathematical shift functions).

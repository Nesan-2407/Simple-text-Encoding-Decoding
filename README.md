# 🔒 Simple Text Encoder/Decoder (Caesar Cipher)

## 📝 Project Title
Simple Text Encoder/Decoder

## 📄 Overview of the Project
This project is a Command-Line Interface (CLI) tool that implements the **Caesar Cipher**—a simple substitution cipher—for encoding and decoding text. It demonstrates fundamental programming concepts such as string manipulation, character-to-ASCII conversion, and modular design.

## ✨ Features
* **Encoding Mode (-e):** Shifts alphabetic characters forward by an integer key.
* **Decoding Mode (-d):** Shifts alphabetic characters backward by the same key, reversing the encoding.
* **Wrap-Around Logic:** Correctly handles shifts that go past 'Z' or 'z' (e.g., 'Z' shifted by 1 becomes 'A').
* **Preservation:** Non-alphabetic characters (spaces, numbers, punctuation) are preserved and not encrypted.

## 🛠 Technologies/Tools Used
* **Language:** Python 3.x
* **Libraries:** `sys`, `argparse` (standard Python libraries only).
* **VCS:** Git.

## ⚙️ Steps to Install & Run the Project
1.  **Clone the repository:** `git clone <Your-Repo-Link>`
2.  **Navigate to the directory:**
    `cd encoder_decoder`
3.  **Run in Encode Mode (Example: Shift 'hello' by 3):**
    `python main_cli.py -e "hello world" 3`
4.  **Run in Decode Mode (Example: Decode the result, 'khoor zruog', by 3):**
    `python main_cli.py -d "khoor zruog" 3`

## 🧪 Instructions for Testing
* **Functional Test (Reversibility):**
    1.  Encode a phrase with a key (e.g., key 5).
    2.  Take the exact encoded output and decode it using the same key 5.
    3.  Verify that the decoded output is identical to the original phrase.
* **Edge Case Test (Wrap-Around):**
    * Test encoding 'Z' with a key of 2. The output should be 'B'.
* **Error Handling Test:**
    * Try running: `python main_cli.py -e "text" non_number`. The system should output a clean error message and not crash.
### 🔄 Program Logic and Flow

The application follows a strict sequential flow, handling user input, validating data, and making a single core decision (Encode or Decode). The use of a **Try-Except** block ensures the application handles invalid input gracefully (Reliability NFR).

#### 1. Execution Flow Diagram (Conceptual)

The program's structure is sequential and decision-based:

1.  **Start**
2.  **Input/Setup:** Collect Mode, Text, and Key.
3.  **Validation Check:** Enters **Try Block**.
    * Validate Mode (1 or 2).
    * Validate Key (Must be Integer).
4.  **Decision:** Based on the validated Mode, calls the appropriate core function.
    * If **Mode 1 (Encode)**: Calls `encode_text()`.
    * If **Mode 2 (Decode)**: Calls `decode_text()`.
5.  **Output:** Prints the formatted result.
6.  **Error Handling (Except Block):** If any validation fails, the program prints a custom error message and stops.

#### 2. Detailed Process Steps

| Step | Component Involved | Action Performed | Control Flow |
| :--- | :--- | :--- | :--- |
| **I. Initialization** | `run_interactive_cipher()` | Displays menu and prompts for Mode, Text, and Key. | Enters `try` block for validation. |
| **II. Validation (1)** | **Mode Check** | Confirms user input for Mode is exactly '1' or '2'. | Jumps to `except` block on failure. |
| **III. Validation (2)** | **Key Conversion** | Attempts to convert the `shift` input string to an integer. | Jumps to `except` block on failure. |
| **IV. Core Decision** | Conditional Statement | Determines if the flow proceeds to Encoding or Decoding. | `if mode == '1'` |
| **V. Execution** | `encode_text()` OR `decode_text()` | Calls the core logic, iterating through the text and applying the character shift. | Executes the selected function. |
| **VI. Output** | `run_interactive_cipher()` | Formats and prints the final `Processed Text`. | Exits the `try` block successfully. |
**Input:** Mode 1, Text: `encode`, Key: 1.
**Output (Cipher Text):** `fodpef`

The character 'e' shifts one position forward to 'f', 'n' shifts to 'o', and so on.

![Console Output showing the encoding of "encode" to "fodpef" with key 1](image_de9d9e.png)

#### B. Execution 2: Decoding ("fodpef" with Key 1)

**Input:** Mode 2, Text: `fodpef`, Key: 1.
**Output (Plain Text):** `encode`

The process is reversed: the character 'f' shifts one position backward to 'e', confirming the integrity of the decryption.

![Console Output showing the decoding of "fodpef" back to "encode" with key 1](image_de9d85.png)

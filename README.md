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

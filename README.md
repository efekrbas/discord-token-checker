# Discord Token Checker

A Python tool for validating Discord tokens using the Discord Gateway WebSocket API.

## Features

- ✅ Validates Discord tokens via WebSocket connection
- 🚀 Asynchronous processing for fast validation of multiple tokens
- 📝 Automatically removes invalid tokens from your list
- 🔄 Auto-installs required dependencies

## Requirements

- Python 3.7+
- `websockets` library (auto-installed if missing)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.7+ installed

```bash
git clone https://github.com/yourusername/discord-token-checker.git
cd discord-token-checker
```

## Usage

1. Add your tokens to `tokens.txt` (one token per line)

```txt
your_token_here
another_token_here
```

2. Run the validator

```bash
python checker.py
```

3. The script will:
   - Connect to Discord Gateway for each token
   - Validate each token asynchronously
   - Display valid tokens with their usernames
   - Update `tokens.txt` with only valid tokens

## Example Output

```
==================================================
   Token Validation and Cleanup
==================================================

Checking 5 tokens...

[+] Valid: username1
[+] Valid: username2
[-] Invalid token
[-] Invalid: Connection closed...
[+] Valid: username3

==================================================
Valid: 3/5
==================================================

[+] tokens.txt updated! Only 3 valid tokens remain.
```

## File Structure

```
discord-token-checker/
├── checker.py            # Main validation script
├── tokens.txt            # Token list (one per line)
└── README.md             # This file
```

## How It Works

1. Reads tokens from `tokens.txt`
2. Connects to Discord Gateway (`wss://gateway.discord.gg`)
3. Sends an Identify payload with each token
4. If the Gateway responds with `READY`, the token is valid
5. Invalid tokens are filtered out and `tokens.txt` is updated

## Notes

- Comments (lines starting with `#`) in `tokens.txt` are ignored
- Tokens can be wrapped in quotes (`"token"` or `'token'`)
- Empty lines are automatically skipped
- The script handles Windows console encoding issues automatically

## Disclaimer

⚠️ **Educational purposes only.** Use responsibly and in accordance with Discord's Terms of Service. The developers are not responsible for any misuse of this tool.

## License

MIT License

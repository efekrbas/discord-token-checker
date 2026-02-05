import asyncio
import json
import os
import sys

# Windows console encoding fix
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import websockets
except ImportError:
    os.system("pip install websockets")
    import websockets

GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json"

async def validate_token(token):
    """Check if the token is valid"""
    try:
        async with websockets.connect(GATEWAY_URL) as ws:
            # Receive Hello message
            await ws.recv()
            
            # Send Identify payload
            identify_payload = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "os": "windows",
                        "browser": "chrome",
                        "device": "pc"
                    },
                    "intents": 513
                }
            }
            await ws.send(json.dumps(identify_payload))
            
            # Wait for response
            response = await asyncio.wait_for(ws.recv(), timeout=10)
            data = json.loads(response)
            
            if data.get("t") == "READY":
                username = data["d"]["user"]["username"]
                print(f"[+] Valid: {username}")
                return True, token
            else:
                print(f"[-] Invalid token")
                return False, token
                
    except Exception as e:
        print(f"[-] Invalid: {str(e)[:50]}")
        return False, token

async def main():
    print("=" * 50)
    print("   Token Validation and Cleanup")
    print("=" * 50)
    
    # Read existing tokens
    tokens = []
    with open("tokens.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            token = line.strip('"').strip("'")
            if token:
                tokens.append(token)
    
    print(f"\nChecking {len(tokens)} tokens...\n")
    
    # Validate each token
    tasks = [validate_token(token) for token in tokens]
    results = await asyncio.gather(*tasks)
    
    # Filter valid tokens
    valid_tokens = [token for is_valid, token in results if is_valid]
    
    print(f"\n" + "=" * 50)
    print(f"Valid: {len(valid_tokens)}/{len(tokens)}")
    print("=" * 50)
    
    # Update tokens.txt file
    with open("tokens.txt", "w", encoding="utf-8") as f:
        f.write("# Valid tokens (verified)\n")
        for token in valid_tokens:
            f.write(f"{token}\n")
    
    print(f"\n[+] tokens.txt updated! Only {len(valid_tokens)} valid tokens remain.")

if __name__ == "__main__":
    asyncio.run(main())

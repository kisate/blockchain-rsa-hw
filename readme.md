# Usage
## Generate
```bash
python main.py -c generate -o key
```
Generate keys and save them as "key" file
## Sign
```bash
python main.py -c sign -o sign -i input.txt -k key
```
Sign text from "input.txt" with generted keys from "key" and save the signature as "sign"
## Verify
```bash
python main.py -c verify -i input.txt -k key -s sign
```
Verify signature from "sign" for message "input.txt" with keys from "key"
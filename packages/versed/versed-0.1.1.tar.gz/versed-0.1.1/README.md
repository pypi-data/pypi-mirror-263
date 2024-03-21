# versed
A command line app to aid in scripture memorization. "I have stored up your word in my heart, that I might not sin against you." Psalm 119:11

## How to Install

```bash
pip install versed
```

## How to Use

To initialize a new `.versed` file. This is the local storage location where you should place your ESV API token. Without an ESV API token, this command line app will not function.

```bash
python -m versed init
```

Navigate to the .versed file and paste your token in.

Retrieve a scripture:

```bash
python -m select-verse 'psalm 27:4'
```

Retrieve and pretty print the verse passage only (requires jq):
```bash
python -m versed select-verse 'psalm 27:4' | jq '.passages[0]' -r
```

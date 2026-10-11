# jacksum-help2wiki
Converts `jacksum -h` output to a GitHub Wiki compatible markup

## Usage

### macOS
```
jacksum -h | ./help2wiki.py > wiki.txt
jacksum -h | ./help2wiki.py | pbcopy
```

### Windows
```
jacksum -h | .\help2wiki.py > wiki.txt
jacksum -h | .\help2wiki.py | clip
```

### Linux
```
jacksum -h | ./help2wiki.py > wiki.txt
jacksum -h | ./help2wiki.py | wl-copy  # Ubuntu, Debian, etc.
jacksum -h | ./help2wiki.py | xclip -selection clipboard  # other distries
```


# parseCaps.py

Parse .cap files with multiple network handshakes into individual .caps for each network.

## Usage
```
python .\parseCaps.py [options] capfile.cap
```

## Options
*  -o, --outfolder : Folder to place all the cap files
*  -n, --networks  : Output names of networks with handshakes

## Example
```
python ./parsecaps.py --outfolder ./ --networks wpa.cap
```

## License
MIT

## Check Ink Levels on HP OfficeJet Pro 6230

![HP PRinter][PrinterImage]

[PrinterImage]: https://store.hp.com/UKStore/Html/Merch/Images/c04339184_500x367.jpg

A Simple Script to check the ink levels via the web interface on the printer.
In its current state it will print a dict of dicts with the results to the shell.

Example output:
```bash
{'Alpha': {'Black': 'Err', 'Cyan': 'Err', 'Magenta': 'Err', 'Yellow': 'Err'},
 'Bravo': {'Black': '70', 'Cyan': '39', 'Magenta': '88', 'Yellow': '12'},
 'Charlie': {'Black': '13', 'Cyan': '100', 'Magenta': '100', 'Yellow': '62'}}
```

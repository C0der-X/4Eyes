# 4Eyes

the 4eyes: Subdomain and domain scans. And this program has the spider feature.
============================================================================
   $ python3 main.py -h

            usage: main.py [-h] [-u URL] [-s SELECT] [-o OUTPUT]

            optional arguments:
              -h, --help  show this help message and exit
              -u URL      enter url: 'https://www.example.com'
              -s SELECT   method: [1]spider, [2]subdomain, [3]domain
              -o OUTPUT   output: noname.txt
  
============================================================================

  $ python3 main.py -u https://www.example.com -s 1 -o output.txt

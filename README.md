# PROJECT DESCRIPTION #
[![MIT licensed][mit-badge]][mit-link]

**UPDATE:** *This project has been updated to be compatible with Python 3*

This Python script allows you to check a list of hashes (provided in the form of a text file) against the virustotal.com database
using their API.

The script takes a text file as an argument, sends each hash to virustotal.com via the API, runs a lightweight python web server locally (on port 8000 by default) and returns the information about the hashes in the form of an HTML table with the following structure:

| hash_value (MD5)  | FORTINET detection names | Number of engines detected | Scan Date |
|-------------------|--------------------------|----------------------------|-----------|

Example:
![alt Output example](./img.png)

The `index.html` file will be generated, holding the last query's results.

NOTE:
Virustotal sets the quota - 4 API Queries per 1 minute, so the script is using a 15-second delay for each hash listed in
the file.

## Dependencies ##
Install Python with homebrew (pip will be installed automatically in this case):

    brew install python

Install virustotal-api using pip:

    pip install virustotal-api

The previous version of this project used an external HTML.py module which appears to only be compatible with Python 2. For Python 3, this project uses the simpletable.py module from [here](https://github.com/matheusportela/simpletable).

You will also need to supply the script with your VirusTotal API key. You can add the key to `keylist.py.template` and save the file as `keylist.py`.


## Usage ##
Running script example:

    python virustotal.py sample_hash_input.txt

To see the results report navigate to `http://localhost:8000` in the browser.

If another port needs to be used, please run the script with the `--port` switch:

    python virustotal.py sample_hash_input.txt --port 8080

OR:

    python virustotal.py sample_hash_input.txt -p 8080


## Credit ##
Original project created by:
Andrew Shagayev | [GitHub](https://github.com/drew-kun)

Simpletable Python module created by:
Matheus Portela | [GitHub](https://github.com/matheusportela)


[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-link]: https://raw.githubusercontent.com/drew-kun/virustotal-api-hashcheck/master/LICENSE

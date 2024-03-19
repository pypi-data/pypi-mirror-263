## PyUnTarZip
PyUnTarZip is a simple Python tool for compressing and decompressing files in ZIP and TAR formats.
## Installation
To install PyUnTarZip, you can use pip:
```sh
pip install PyUnTarZip
```
## Usage
PyUnTarZip offers the following commands for compressing and decompressing files:
### Compressing Files
To compress a file in ZIP format, use the following command:
```sh
python -m PyUnTarZip compact zip <file path> <destination path>
```
To compress a file in TAR format, use the following command:
```sh
python -m PyUnTarZip compact tar <file path> <destination path>
```
### Decompressing Files
To decompress a file in ZIP format, use the following command:
```sh
python -m PyUnTarZip extract zip <file path> <destination path>
```
To decompress a file in TAR format, use the following command:
```sh
python -m PyUnTarZip extract tar <file path> <destination path>
```
Replace <file path> with the path of the file you want to compress or decompress, and <destination path> with the directory where you want to save the compressed or decompressed file.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
import tarfile
import zipfile

def compactar_zip(arquivos, destino):
    with zipfile.ZipFile(destino, 'w') as zip_ref:
        for arquivo in arquivos:
            zip_ref.write(arquivo)

def compactar_tar(arquivos, destino):
    with tarfile.open(destino, 'w') as tar_ref:
        for arquivo in arquivos:
            tar_ref.add(arquivo)

def extrair_zip(arquivo, destino):
    with zipfile.ZipFile(arquivo, 'r') as zip_ref:
        zip_ref.extractall(destino)

def extrair_tar(arquivo, destino):
    with tarfile.open(arquivo, "r") as tar:
        tar.extractall(path=destino, members=tar.getmembers(), filter='data')
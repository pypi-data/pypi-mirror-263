import os
import argparse
from PyUnTarZip.__init__ import compactar_zip,compactar_tar,extrair_zip,extrair_tar

def main():
    parser = argparse.ArgumentParser(description="Compacta ou descompacta arquivos ZIP ou TAR")
    parser.add_argument("acao", choices=["compact", "extract"], help="Ação a ser executada: compact ou extract")
    parser.add_argument("tipo", choices=["zip", "tar"], help="Tipo de arquivo: zip ou tar")
    parser.add_argument("arquivo", help="Caminho para o arquivo a ser compactado/descompactado")
    parser.add_argument("destino", help="Caminho para o diretório de destino")

    args = parser.parse_args()

    if args.acao == "compact":
        if args.tipo == "zip":
            compactar_zip([args.arquivo], args.destino)
        elif args.tipo == "tar":
            compactar_tar([args.arquivo], args.destino)
    elif args.acao == "extract":
        if args.tipo == "zip":
            extrair_zip(args.arquivo, args.destino)
        elif args.tipo == "tar":
            extrair_tar(args.arquivo, args.destino)

if __name__ == "__main__":
    main()

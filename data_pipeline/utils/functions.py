import zipfile
import os

def compress_files(source_folder, file_name, output_folder):
    """
    Função responsável por salvar todos os arquivos dentro do parâmetro "source_folder",
    E compila nomeado com "file_name" dentro de "output_folder"
    """
    output_path = os.path.join(output_folder, file_name)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_folder))

    print(f"Arquivos compactados e salvos em {output_folder}")
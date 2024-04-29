import subprocess
import os

def instalar_programas_do_pendrive(letra_unidade_pendrive):
    # Caminho da unidade do pen drive
    caminho_pendrive = f"{letra_unidade_pendrive}D:\Agro7"

    # Lista de programas para instalar (aqui estou assumindo que os arquivos de instalação estão no diretório 'Programas')
    Agro7 = os.path.join(caminho_pendrive, "7z2404-x64.exe", "ChromeSetup.exe", "Firefox Installer", "Protheus-12.2210-Install")
    
    # Verificar se o diretório existe
    if not os.path.exists(Agro7):
        print(f"O diretório 'Agro7' não existe na unidade {letra_unidade_pendrive}.")
        return

    # Percorrer os arquivos de instalação no diretório 'Programas'
    for arquivo in os.listdir(Agro7):
        # Obter o caminho completo do arquivo
        caminho_arquivo = os.path.join(Agro7, arquivo)
        
        # Verificar se o arquivo é um executável
        if caminho_arquivo.endswith(".exe"):
            print(f"Instalando {caminho_arquivo}...")
            # Argumentos para instalação silenciosa
            args_instalacao = ["/S"]
            
            # Executar o arquivo de instalação com argumentos
            try:
                subprocess.run([caminho_arquivo] + args_instalacao)
                print(f"{caminho_arquivo} instalado com sucesso!")
            except Exception as e:
                print(f"Erro ao instalar {caminho_arquivo}: {e}")

# Exemplo de uso: especifique a letra da unidade do pen drive
letra_unidade_pendrive = ""  # Substitua pela letra da unidade do pen drive
instalar_programas_do_pendrive(letra_unidade_pendrive)


<a href='https://github.com/Junwu0615/Ansible-Deploy-To-Edge'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Ansible-Deploy-To-Edge.svg'>
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Project-Ansible_Deploy_To_Edge-blue.svg?style=plastic)](https://github.com/Junwu0615/Ansible-Deploy-To-Edge)
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/Junwu0615/Ansible-Deploy-To-Edge) <br>

<br>

## *⭐ 建置 WSL 環境 ⭐*

### *A.　設置 WSL 2 # 如果尚未設置*
- #### *啟用 WSL 2 # 在 PowerShell 中執行*
    ```powershell
    wsl --install
    ```
  - ##### *[ 繼續設定步驟.1 ] 創建使用者名稱*
    ```powershell
    Enter new UNIX username: yourname
    ```
  - ##### *[ 繼續設定步驟.2 ] 設定密碼*
    ```powershell
    New password: 
    Retype new password: 
    ```
  - ##### *設定完成*

- #### *[安裝 Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) : 確保 Docker Desktop 運行在 WSL 2 後端*

<br>

### *B.　準備 Ansible 和 Docker*
- #### *更新系統*
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

- #### *安裝 Python 和 Ansible #  Ansible 需要 Python 才能運行*
    ```bash
    sudo apt install python3 python3-pip ansible -y
    ```
  
- #### *安裝 SSH Server # 確保你的 WSL 環境可以作為 Ansible 的目標被連線*
    ```bash
    sudo apt install openssh-server
    ```
  - ##### *啟動 SSH 服務*
    ```bash
    sudo service ssh start
    ```

  - ##### *確認服務正在運行*
    ```bash
    service ssh status
    ```

<br>
<a href='https://github.com/Junwu0615/Ansible-Deploy-To-Edge'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Ansible-Deploy-To-Edge.svg'>
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Project-Ansible_Deploy_To_Edge-blue.svg?style=plastic)](https://github.com/Junwu0615/Ansible-Deploy-To-Edge)
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/Junwu0615/Ansible-Deploy-To-Edge) <br>

<br>

## *⭐ 準備部署 Images & 腳本 ( 提供範例 ) ⭐*

- #### *A.　確認專案路徑是否有範例腳本*
- ![PNG](../sample/script.PNG)

<br>

- #### *B.　先行部署測試能否正常運行*
  - #### *STEP.1　Enter Docker Path*
    ```bash
    cd docker
    ```

  - #### *STEP.2　Dockerfile Build Image*
    ```bash
    docker build -t pc-hello-world:latest -f script/Dockerfile . --no-cache
    ```
  
  - #### *STEP.3　Docker Compose Up*
    ```bash
    docker stack deploy -c script/docker-compose.yaml pc-hello-world
    ```
  
  - #### *STEP.4　檢視服務啟動狀態*
    ```bash
    docker service ls
    docker service logs -f pc-hello-world_task
    ```
  
  - #### *STEP.5　移除服務*
    ```bash
    docker stack rm pc-hello-world
    ```
    
  - ![PNG](../sample/test_success.PNG)
    
<br>

- #### *C.　上傳腳本至 Docker-Registry ( 須提前建置 )*
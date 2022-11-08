# [How to] Install mysql 5.7
- Copy the key [here](https://alx-intranet.hbtn.io/rltoken/Zzs_TLRYjWWFxjJRArmFcQ) to your clipboard

- Save it in a file on your machine i.e. signature.key and then
```sh
sudo apt-key add signature.key
```
- add the apt repo
```sh
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
```
- update apt
```sh
sudo apt-get update
```
- now check your available versions:
```sh
vagrant@ubuntu-focal:/vagrant$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```
- Now install mysql 5.7
```sh
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```
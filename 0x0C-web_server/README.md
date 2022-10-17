# 0x0C. Web server
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

A good Software Engineer is a [lazy Software Engineer.](https://alx-intranet.hbtn.io/rltoken/sRY__axKNHhNW0SVmsUC_A)
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

## Tasks

### [Task 0. Transfer a file to your server](./0-transfer_file)
Write a Bash script that transfers a file from our client to a server:

**Requirements:**

- [x] Accepts 4 parameters
  1. [x] The path to the file to be transferred
  1. [x] The IP of the server we want to transfer the file to
  1. [x] The username `scp` connects with
  1. [x] The path to the SSH private key that `scp` uses
- [x] Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- [x] `scp` must transfer the file to the user home directory `~/`
- [x] Strict host key checking must be disabled when using `scp`


### [1. Install nginx web server](./1-install_nginx_web_server)
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221017%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221017T161358Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5e7b198a6022d095446aed1ac1feb49b7ca3746069dcd12b0315b589958af476)

**Readme:**

[-y on apt-get command](https://alx-intranet.hbtn.io/rltoken/KJiFZ4yJyTGp_cv3DYQLaQ)
*Web servers are the piece of software generating and serving HTML pages, let’s install one!*

**Requirements:**

- [x] Install `nginx` on your `web-01` server
- [x] Nginx should be listening on port 80
- [x] When querying Nginx at its root `/` with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- [ ] As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- [x] You can’t use `systemctl` for restarting `nginx`
Server terminal:
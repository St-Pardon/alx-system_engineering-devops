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
77;30407;0c  1. [x] The IP of the server we want to transfer the file to
  1. [x] The username `scp` connects with
  1. [x] The path to the SSH private key that `scp` uses
- [x] Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- [x] `scp` must transfer the file to the user home directory `~/`
- [x] Strict host key checking must be disabled when using `scp`


### [1. Install nginx web server](./1-install_nginx_web_server)

**Readme:**

[-y on apt-get command](https://alx-intranet.hbtn.io/rltoken/KJiFZ4yJyTGp_cv3DYQLaQ)
*Web servers are the piece of software generating and serving HTML pages, let’s install one!*

**Requirements:**

- [x] Install `nginx` on your `web-01` server
- [x] Nginx should be listening on port 80
- [x] When querying Nginx at its root `/` with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
- [x] As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- [x] You can’t use `systemctl` for restarting `nginx`
Server terminal:

### [2. Setup a domain name](./2-setup_a_domain_name)
**Requirement:**

- [x] provide the domain name only (example: foobar.tech), no subdomain (example: `www.foobar.tech`)
- [x] configure your DNS records with an A entry so that your root domain points to your `web-01` IP address **Warning: the propagation of your records can take time (~1-2 hours)**
- [x] go to your profile and enter your domain in the `Project website url` field

### [3. Redirection](./3-redirection)
**Readme:**

[Replace a line with multiple lines with sed](https://alx-intranet.hbtn.io/rltoken/RRP9hX3MlQdABaKZD-Y_cA)
*Configure your Nginx server so that `/redirect_me` is redirecting to another page.*

**Requirements:**

- [x] The redirection must be a “301 Moved Permanently”
- [x] You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- [x] Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

### [4. Not found page 404](./4-not_found_page_404)

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

**Requirements:**

- [x] The page must return an HTTP 404 error code
- [x] The page must contain the string `Ceci n'est pas une page`
- [x] Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task
# 0x0C. Web server
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

A good Software Engineer is a [lazy Software Engineer.](https://alx-intranet.hbtn.io/rltoken/sRY__axKNHhNW0SVmsUC_A)
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

## Tasks

### Task 0. Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

**Requirements:**

- [ ] Accepts 4 parameters
      1 The path to the file to be transferred
      2 The IP of the server we want to transfer the file to
      3 The username `scp` connects with
      4 The path to the SSH private key that `scp` uses
- [ ] Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- [ ] `scp` must transfer the file to the user home directory `~/`
- [ ] Strict host key checking must be disabled when using `scp`
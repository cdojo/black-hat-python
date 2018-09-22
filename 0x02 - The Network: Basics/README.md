# 2. The Network: Basics

This chapter will give you some basics on Python networking using the **socket** module.
Let's get started.

## TCP Client

There have been countless times during penetration tests that I've needed to ship up a TCP client to test for services, send garbage data, fuzz, or any number of other taks.
If you are working within the confines of large enterprise environments, you won't have the luxury of networking tools or compilers, and sometimes you'll even be missing the absolute
basics like the ability to copy/paste or an Internet connection. This is whre beign able to quickly create a TCP client comes in a extremely handy. Here is a simple [TCP Client](https://github.com/cdojo/black-hat-python/blob/master/0x02%20-%20The%20Network:%20Basics/code/tcp_client.py)

## UDP Client

A Python UDP client is not much different than a TCP client, we change the socket type to **SOCK_DGRAM** when creating the socket object.

## TCP Server

## TCP proxy

```
./tcp_proxy.py 127.0.0.1 21 ftp.target.com 21 True
```

## SSH with Paramiko

* bh_sshcmd.py

```
pip install paramiko
```

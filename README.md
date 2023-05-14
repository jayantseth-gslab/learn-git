# Welcome to the git tutorial

We are together going to build The Ping App, which takes list of ips in excel, pings them and records the output in another excel.

And while we are building this app we will learn about how git is actually a <del>life</del> time & effort savior.

So let's begin:

To Start with, please download/clone this repo, it has some initial files to start with and some other files I have given seperately and I'll explain why on the session.

## Pre-requisites:
1. Install python virtual env & activate the same by using following link: [python-virtual-env-install-and-activate](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
2. Install dependencies with below command:
```
pip install -r requirements.txt
```

## Follow below steps to complete the tutorial


1. Create a feature branch for reading data from excel
`git checkout -b feature-read-excel`
2. Apply `get_ips_excel.patch`
`git apply patches/get_ips_excel.patch`
3. Add and commit the changes
`git commit -a 
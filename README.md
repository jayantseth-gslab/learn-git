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

1. Create a feature branch for optimization of ping module
`git checkout -b optimize-ping`
2. Apply `ping_optimization.patch`
`git apply patches/ping_optimization.patch`
3. Add & commit the changes
`git add ping.py && git commit -m "optimized ping"`
4. Git push to remote
`git push origin optimize-ping`

### Branch creation, Branch Merge, Conflict Resolution
1. Create a feature branch for reading data from excel
`git checkout -b feature-read-excel`
2. Apply `get_ips_excel.patch`

    `git apply patches/get_ips_excel.patch`

3. Add and commit the changes

    `git add excel_util.py && git commit -m "added excel read method"`
4. Checkout to master branch

    `git checkout master` or `git switch master`

5. Create a feature branch for writing data to excel

    `git checkout -b feature-write-excel`
6. Apply `write_data_excel.patch`

    `git apply patches/write_data_excel.patch`

7. Add and commit the changes

    `git add excel_util.py && git commit -m "added method to write data to excel"`

Merging the changes from two branches

8. Switch to master branch

    `git checkout master` or `git switch master`

9. Merge `feature-read-excel` branch

    `git merge feature-read-excel`

10. Merge `feature-write-excel` branch

    `git merge feature-write-excel`

There will be conflict as both branches did the changes in the same file, resolve them manually or use vscode for the same


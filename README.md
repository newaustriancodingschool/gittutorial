# Git Tutorial
RSA entcryption/decryption that reads and writes into a file. This task will be written in Python.

## Clone this project for group A & B
use the command
```
git clone git@github.com:RefugeesCodeAT/gittutorial.git
```
***
## Group A
```
git checkout encryption
```
## Group B
```
git checkout decryption
```
## Merging
First you need to find a partner from the other team.
You don't want to work on my github branch so we are going to change the origin to one of you.
For this task go together with your partner and choose one notebook.
You can see your current remotes (*origin* in our case) with following command:
```
git remote -v
```
Change it to your partners IP-address and then check again.
```
git remote set-url origin ssh://
```
There you have to change into the master branch:
```
git checkout master
```
We want to merge both branches (encryption and decryption) into master. After that we want to push our code so your partner can use your code.
```
git merge encryption
git merge decryption
git commit -m "merge encryption and decryption into master"
git push
```
Go to the other notebook and checkout the updated master:
```
git checkout master
git pull
```
If you enter *git log* you should see the commits of your partner and if you run the test both test cases should execute.

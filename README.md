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
After that you should be able to see the *encrypt_and_write* method in [mycrypto.py](crypto/mycrypto.py).
This method requires three parameters, namely *message*, *keyname* and *write_to*.
Your task is to implement the encryption using RSA. Therefore you have to load the public key of your partner and encrypt the given message with this key. Your partner should be able to read this message with his/her private key.
To implement this task you have to do the following steps. (feel free to change the [markdown](README.md)) if you completed the steps.

- [ ] load the public key as a string from *filename*. Hint: use *myfile*
- [ ] convert string into RSA key. Hint: use *RSA.importKey()*-Method
- [ ] encode the message as 'utf-8'. Therefore look at the string API
- [ ] encrypt the *message*
- [ ] write the encrypted text to a file: Hint: use *myfile*. To use this method you have to convert the encrypted text to a string.
- [ ] **commit your task and push it**

### Testing
Go to commandline and enter
```
phyton
```
There you should see the python shell starting with *>>>*
```python
>>> from crypto.test import test
>>> test.test()
```
To exit the shell press *Ctrl+D*

## Group B
```
git checkout decryption
```
After that you should be able to see the *decryption_and_return* method in [mycrypto.py](crypto/mycrypto.py).
This method requires two parameters, namely *filename* and *keyname*.
Your task is to implement the decryption using RSA. Therefore you have to load your private key and decrypt the encrypted message from *filename* with this key. You should be able to read this message.
To implement this task you have to do the following steps. (feel free to change the [markdown](README.md)) if you completed the steps.

- [ ] load the private key as a string from *filename*. Hint: use *myfile*
- [ ] convert the string into RSA key. Hint: use *RSA.importKey()*-Method
- [ ] load the encrypted text. Hint: use *myfile*
- [ ] convert the encrypted text from a string to binary. Hint: use
```python
ast.literal_eval(str)
```
- [ ] decrypt the message
- [ ] decode the decrypted text as 'utf-8'. Therefore look at the string API
- [ ] print decrypted text
- [ ] **commit your task and push it**

### Testing
Go to commandline and enter
```
phyton
```
There you should see the python shell starting with *>>>*
```python
>>> from crypto.test import test
>>> test.test()
```
To exit the shell press *Ctrl+D*
***
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

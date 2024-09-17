# Answer 1:
Synchronous :The signal handler runs right after the record is saved, in the same process and thread. The code waits for the signal handler to finish before moving on.
Asynchronous: If signals were asynchronous, the handler might run later, possibly in a different thread or process. Django would need extra setup to handle this, which is not the default behavior.
# By default, Django executes signals synchronously. This indicates that when a signal is sent, the receiver functions are started on the same thread as the signal sender right away.

![image](https://github.com/user-attachments/assets/032146bc-69e6-4d4c-9c1a-7af815749cd6)
![image](https://github.com/user-attachments/assets/9a654feb-454f-4d7c-989d-7afa93c14ad6)

When you run this github code, and create a superuser you’ll immediately see "User save Instance" printed out, showing that the handler runs right away.

# Answer 2:
Yes, the caller and Django signals operate on the same thread. This indicates that the receiver functions run in the same thread and process as the signal that generated it. Using threading, we can demonstrate that the signal handler executes on the same thread as the code that initiated it.



![image](https://github.com/user-attachments/assets/ae0f89c8-fab4-47d9-a405-79e1d1bbea45)
Last line prints a message including the thread ID where the user_save function is running. threading.get_ident() returns the ID of the current thread.
![image](https://github.com/user-attachments/assets/156edcdd-ea65-4278-b08c-3049d3c1e822)
this View function create a new user with username and password also its print the thread id 

![image](https://github.com/user-attachments/assets/2ce2f3bb-0196-41f4-8e19-658491546a1e)
we can observe that the signal handler executes in the same thread as the saving process, which confirms that Django signals are synchronous and run in the same thread as the action that triggered them.

# Answer 3: 
![image](https://github.com/user-attachments/assets/3eb095ea-bfc2-430a-9ad6-8c114501bf9f)
![image](https://github.com/user-attachments/assets/fcfcd09f-167c-46cc-82aa-0ea07796bb2a)
![image](https://github.com/user-attachments/assets/38102c8a-e51e-4a5b-be1c-0b1e5f03866c)
![image](https://github.com/user-attachments/assets/0e630a5d-1511-4ab5-a316-0866632f0a70)

 The user_save function is connected to the post_save signal of the User model. It will execute when a User instance is saved. If the username is 'error_user', it raises an error to force a rollback.
 The view uses transaction.atomic() to ensure that the operation is wrapped in a transaction. If an error occurs, the transaction will be rolled back, and any changes made within the transaction will be undone.
 #  by default, run within the same database transaction as the action that triggered them. When we force an error during the transaction, both the main operation and the signal handler's changes are rolled back together, confirming that they operate within the same transaction scope.








 # Custom Classes in Python

![image](https://github.com/user-attachments/assets/25ec0f11-c512-4711-a6ae-27a903418ce1)


it will print : {'length': 20}
                {'width': 55}
 

# Peer-to-Peer-Chat

Flask, web application/ python application

MySQL

Python socket

One table for sending, one table for receiving

### User Table
User ID | User Name| IP_address
-|-|-
000 | 123 | Jack 
001 | 456 | Alice
002 | 789 | Bob

### Message Table
IP_address|      User_name|      Message|    Message_status | Message_time
-|-|-|-| -
123 | Jack | hhh | pending | 300 
456 | Alice | ddd | sent | 365
789 | Bob | uuu | failed | 280

### Session Table
Session ID | User 
-|-
0000 | 123
0001 | 456
0002 | 789

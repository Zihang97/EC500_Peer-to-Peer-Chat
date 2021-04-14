# Peer-to-Peer-Chat

For database, we use mysql and build three tables. One table serving as address book to record user information, one table for sending and the last table for receiving.

### User Table
User Name| IP_address
-|-
Jack| 0.0.0.1
Alice | 0.0.0.2
Bob | 0.0.0.3

### Message Table
IP_address|      User_name|      Message|    Message_status | Message_time
-|-|-|-| -
0.0.0.1 | Jack | hhh | pending | 300 
0.0.0.2 | Alice | ddd | sent | 365
0.0.0.3 | Bob | uuu | failed | 280


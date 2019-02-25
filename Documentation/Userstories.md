# User stories

   As a user I can view all the discussions as a list
   
       SELECT Account.username as username, Discussion.id as d_id, 
                Discussion.account_id as a_id, Discussion.title as title, Discussion.date_created as d_date_created, 
                COUNT(Message.id) as totalmessages, MAX(Message.date_created) as latest_message 
                FROM account INNER JOIN Discussion ON Discussion.account_id=Account.id 
                LEFT JOIN Message ON Message.discussion_id=Discussion.id 
                GROUP BY Discussion.title, Account.username, Discussion.id ORDER BY latest_message DESC

   As a user I can view a single discussion and all its messages
   
     SELECT Account.username AS account_username, 
                Account.date_created AS account_date_created, 
                Message.content AS message_content, 
                Message.date_created AS message_date_created,  
                Message.date_modified AS message_date_modified, 
                Message.account_id as a_id, Message.id as m_id 
                FROM Account, Message, Discussion WHERE Account.id = Message.account_id 
                AND Discussion.id = Message.discussion_id 
                AND Discussion.id = :id 
                ORDER BY Message.date_created

   As a user I can register to the website
    
       INSERT INTO Account(id, username, password)
       VALUES(:id, :username, :password)

   As a user I can login to the website
   
       SELECT*FROM Account WHERE username = :username
       
       Then compare passwords
 
   
   As a user I can search discussions by their tags and title
   
       SELECT account.id as account_id, account.username, discussion.id, 
                discussion.date_created, discussion.date_modified, discussion.title 
                FROM account INNER JOIN discussion on  account.id=discussion.account_id WHERE discussion.id IN
                  (SELECT distinct discussion.id from discussion 
                  INNER JOIN discussion_tag ON discussion.id=discussion_tag.discussion_id 
                  INNER JOIN tag on discussion_tag.tag_id=tag.id 
                  WHERE tag.name LIKE :name)
                  
       SELECT account.id as account_id, Account.username, discussion.id, discussion.date_created, discussion.date_modified, discussion.title 
       FROM Account INNER JOIN discussion ON account.id=discussion.account_id WHERE discussion.title LIKE :name

   As an authenticated user I can create a new discussion
   
       INSERT INTO Discussion(id, title, account_id) 
       VALUES(:id, :title, :account_id)
       
       INSERT INTO tag(id, name, discussion_id)
       VALUES(:id, :name, :discussion_id)
   
   As an authenticated user I can comment on a discussion
       
       INSERT INTO  Message(id, content, account_id, discussion_id)
       VALUES(:id, :content, :account_id, :discussion_id)
   
   As an authenticated user I can view my profile
       
       SELECT Account.username, Account.id, Account.date_created, Account.role, 
       COUNT(Message.id) as total_messages from Account 
       LEFT JOIN Message ON Message.account_id = Account.id WHERE Account.id = :id 
       GROUP BY Account.username, Account.id
   
   As an authenticated user I can change my password
   
       UPDATE Account SET password = :password WHERE Account.id = :id
   
   As an authenticated user I can delete my account permanently
   
       DELETE FROM Account WHERE Account.id = :id
   
   As an authenticated user I can delete my comments on any discussion
   
       DELETE FROM Message WHERE Message.discussion_id = :id
   
   As an authenticated user I can edit my comments
   
       UPDATE Message SET content = :content WHERE Message.id = :id
   
   As an authenticated user I can delete discussions I have started
   
       DELETE FROM Discussion WHERE Discussion.id = :id
   
   As an admin user I can delete any discussion
   
       DELETE FROM Discussion WHERE Discussion.id = :id
   
   As an admin user I can delete any message
   
       DELETE FROM Message WHERE Message.discussion_id = :id
   
   As an admin user I can view a list of all the users
   
       SELECT username, id FROM Account
   
   As an admin user I can delete any user
   
       DELETE FROM Account WHERE Account.id = :id
   

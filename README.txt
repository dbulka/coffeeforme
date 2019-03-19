Step 1: Create file "coffeeforme.ini" and fill private info like that:
[config]
dbuser=...
dbpassword=...
dbhost=...
dbname=...

Step 2: Open requirements.txt and install essential libraries

Step 3: Start using "Coffeeforme" utility by run /coffeeforme.py

Discription:
/.gitignore - includer objects which must not push to github
/bills - route for saving separete bill(file) with sale details
/core/controllers - includes controllers for manager & salesman roles and application related to commandline arguments
/core/interfaces - include interfaces for user & salesman roles and application which show info related to commandline arguments
/utils/context - config file '.ini' reader
/utils/db_service - connect and manipulate with mysql database
/utils/json_writer - bills (json file) writer
/coffeeforme.sql - mysql database
/queries create db coffeeforme.docx - queries in doc fromat for creating mysql database

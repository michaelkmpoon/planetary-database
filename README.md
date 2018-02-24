This program reads the 8 solar system planets' name, mass and radius from a text (.txt) file and calculates each planet's escape velocity.

Then, the data will be stored in a table via *SQLite* and specific data sets can be accessed by queries such as reading individual planetary info or reading only a planet's name and thier corresponding escape velocities.

Note: when running the code for the first time, change 
```
create_tables =  False
```
to
```
create_tables = True
```
in order to create the database (.db) file. 

Following that, you would revert it when running the code again to prevent an error message.

Below is a sample console output (using PyCharm):

```
>>> db = my_db
>>> get_info_by_name(db, 'Earth')
[('Earth', '5.97e+24', '6.4e+06', '11155.1417516767')]
>>> get_info_by_name(db, 'Jupiter')
[('Jupiter', '1.9e+27', '7.1e+07', '59748.2983433803')]
>>> get_all_escape_vel(db)
[('Mercury', '4282.81449516553'), ('Venus', '10351.6847444839'), ('Earth', '11155.1417516767'), ('Mars', '5011.04662074642'), ('Jupiter', '59748.2983433803'), ('Saturn', '35599.1572933967'), ('Uranus', '21369.1006253998'), ('Neptune', '23099.7835487695')]

```

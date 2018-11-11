#!/usr/bin/env python2

import psycopg2
DBNAME = "news"

# print title of output
print "This is the output from analyze.py\n"

# connect to database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# run query for question 1
query = """
    SELECT title, COUNT(*) AS views
      FROM articles
           JOIN log
           ON '/article/' || articles.slug  = log.path
     GROUP BY title
     ORDER BY views desc
     LIMIT 3;
"""
c.execute(query)
rows = c.fetchall()

# output results for question 1
print "The most popular three articles of all time are:"
for row in rows:
    print "  *", row[0], "--", row[1], "views"
print ""

# run query for question 2
query = """
    SELECT name, views
      FROM authors,
           (SELECT author, COUNT(*) AS views
              FROM articles, log
             WHERE '/article/' || articles.slug  = log.path
             GROUP BY author
             ORDER BY views desc) AS subq
     WHERE authors.id = subq.author;
"""
c.execute(query)
rows = c.fetchall()

# output results for question 2
print "The most popular article authors of all time are:"
for row in rows:
    print "  *", row[0], "--", row[1], "views"
print ""

# run query for question 3
query = """
    SELECT req_tbl.date,
           to_char(100.0*err_tbl.errs/req_tbl.reqs,'FM9D99') AS percent
      FROM (SELECT to_char(time, 'FMMonth dd, yyyy') AS date, COUNT(*) AS reqs
              FROM log
             GROUP BY date) AS req_tbl,
           (SELECT to_char(time, 'FMMonth dd, yyyy') AS date, COUNT(*) AS errs
              FROM log
             WHERE substring(status from 1 for 3) != '200'
             GROUP BY date) AS err_tbl
     WHERE req_tbl.date = err_tbl.date
       AND 100*err_tbl.errs > req_tbl.reqs;
"""
c.execute(query)
rows = c.fetchall()

# output results for question 3
print "Days when more than 1% of requests lead to errors:"
for row in rows:
    print "  *", row[0], "--", row[1], "percent"
print ""

# close database
db.close

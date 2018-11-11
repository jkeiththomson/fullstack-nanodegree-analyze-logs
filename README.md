# Udacity FS Project 1: Analyze Logs

## Description
This is the first project for the Udacity "Full Stack Web Developer" nanodegree program. The goal of the projeect is to answer three questions about a database of newspaper articles and their authors.

## Getting Started
### 1. Set up the virtual machine
This project assumes a Linux virtual machine is already set up and initialized. Instructions for setting up the VM can be found on [the course's website] 
(https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0]).

The VM comes with PostgreSQL and Python2 already installed. 
To start the virtual machine on Mac OSX, open a Terminal and type `vagrant up`

To log into the VM, type `vagrant ssh`

### 2. Set up the database

The VM provides a common folder for sharing files between OSX and Linux. On Linux this folder appears as `/vagrant`

Download the project database [from here] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it. Copy the resulting file (`newsdata.sql`) into the `/vagrant` folder.

To initialize the database, cd into `/vagrant` from the VM's Terminal and run the following command:

`psql -d news -f newsdata.sql`

This creates the tables in the database and fills them with data.

### 3. Set up the code
Clone this project from its GitHub repository and copy the file `analyze.py` into the `/vagrant` folder

## Running the Code
From the VM's Terminal, make sure you're still in the `/vagrant` folder and run the command

`python analyze.py`

The output is displayed on the Terminal.

## Sample Output
The file `analyze.txt` contains a copy of the text that is printed on the console when you run `analyze.py`

## Notes on the Design
The project specification requires that each question be answered by a single SQL query.

The instructions didn't mention a required style for the SQL queries, so I elected to use [Simon Holywell's Style Guide](https://www.sqlstyle.guide/), which emphasizes readability of the SQL code.

### Q1. What are the most popular three articles of all time?

To answer this question, I joined the articles table with the log table. I had to prepend the string `/article/` to the slug column of the articles table so it would match the path column of the log table. Then I just counted the rows in the joined table, grouped by title and ordered by the count.


### Q2. Who are the most popular article authors of all time?

In this case, I created a subquery to count the number of times in the log table that each author's articles were viewed. I joined this subquery with the authors table to match the author IDs with their names.

### Q3. On which days did more than 1% of requests lead to errors? 

Here I created two subqueries, one that counted the total number of requests per day and one that counted the numer  of errors per day, Then I used both tables to query for which days had 1% or more errors.
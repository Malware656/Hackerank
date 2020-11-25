# Hackerank Answer FOr restApi programs

Team_goals.py

Welcome to
HackerRank Rest API (Intermediate) Skills Certification Test


In this challenge, the REST API contains information about football matches. The provided API allows querying matches by teams and year. Your task is to get the total number of goals scored by a given team in a given year.
To access a collection of matches, perform GET requests to
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team2=<team>&page=<page>
where <year> is the year of the competition, <team> is the name of the team, and <page> is the page of the results to request. The results might be divided into several pages. Pages are numbered from 1.

Notice that the above two URLs are different. The first URL specifies the team1 parameter (denoting the home team) while the second URL specifies the team2 parameter (denoting the visiting team). Thus, in order to get all matches that a particular team played in, you need to retrieve matches where the team was the home team and the visiting team.

For example, a GET request to

https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=Barcelona&page=2
returns data associated with matches in the year 2011, where team1 (the home team) was Barcelona, on the second page of the results.
Similarly, a GET request to
https://jsonmock.hackerrank.com/api/football_matches?year=2011&team2=Barcelona&page=1
returns data associated with matches in the year 2011 where team2 (the visiting team) was Barcelona, on the first page of the results.


Team_goals_2.py

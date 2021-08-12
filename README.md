## Splunk Quick Cheat Sheet

**DNS Lookup**
```
| lookup dnslookup clientip as dst OUTPUT clienthost as DST_RESOLVED
```

**Event Frequency**
```
| stats count by signature
    `comment("define varriables")`
| eval days = 10
| eval events_perShift = round(count / ((days * 24)/4),3)
| eval events_perDay = round(count / days,2)
| eval events_perWeek = round(count / (days / 7),2)
| sort - count
| fields - count days
| table signature events_perShift events_perDay events_perWeek
| addcoltotals labelfield=signature label=Total
```

**Get the earliest and latest time for an observed field value**
```
| stats earliest(_time) as firstTime latest(_time) as lastTime by dest
| eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
```

**List All Available Indexes with Events**
```
| eventcount summarize=false index=*
| search count!=0
| dedup index
| fields - server
```

**List All Available Sourcetypes in an Index**
```
| metadata type=sourcetypes index=foo
| eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
| eval recentTime=strftime(recentTime,"%Y-%m-%d %H:%M:%S")
```


**lower case all fields**
```
| foreach "*" [eval <<FIELD>>=lower('<<FIELD>>') ]
```

**make time human readable**
```
eval mytime=strftime(_time,"%Y-%m-%d %H:%M:%S")
```


**get current user context**
```
| rest /services/authentication/current-context splunk_server=loacal
```

**Group By Octet** <br>
2 Octets
```
| rex field=src_ip "(?<subnet>\d+\.\d+)+\.\d+\.\d+"
| stats count by subnet
```
3 Octets
```
| rex field=ip "(?<subnet>\d+\.\d+\.\d+)\.\d+"
| stats count by subnet
```

**use of now**
```
| eval yesterday=relative_time(now(), "-1d@d")
```

**Turn a field in an output into csv format**
```
| stats count by foo
| mvcombine foo delim=","
| nomv foo
```

**expand multivalued field**
```
|| fields foo
| mvcombine foo delim=","
| nomv foo
```

**Search time in a lookup** <br>
Incident Review is used as an example
```
| inputlookup incident_review_lookup
| addinfo
| eval yesterday=relative_time(now(), "-1d@d")
| where (time >= yesterday AND time <= info_max_time)
```

**Find hosts that haven not checked in in a specified amount of time**
```
| stats latest(_time) as lastTime earliest(_time) as firstTime by hostnames
    `comment("change the "-30d" to choose a date that we haven't seen assets check in by")`
| eval recent = if(lastTime > relative_time(now(),"-30d"),1,0), realLatest = strftime(latest,"%c")
| eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
| where recent=0
```

**Join**
```
search | join type=inner
| join type=left max=0 
| join type=inner overwrite=false genre_id
[| {​​​search}​​​​​​​​​​ | rename id as genre_id ]
```

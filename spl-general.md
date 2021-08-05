**get current user**
```
| rest /services/authentication/current-context splunk_server=loacal
| fields realname | rename realname as analyst
```

**lower case all fields**
```
| foreach "*" [eval <<FIELD>>=lower('<<FIELD>>') ]
```

**make time human readable**
```
eval mytime=strftime(_time,"%Y-%m-%d %H:%M:%S")
```

Get the earliest and latest time for an observed field value
```
| stats earliest(_time) as firstTime latest(_time) as lastTime by dest
| eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
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
| stats count by foo
| eval action = split(action,",")
| mvexpand action
```

**Search time in a lookup** <br>
Incident Review is used as an example
```
| inputlookup incident_review_lookup
| addinfo
| eval yesterday=relative_time(now(), "-1d@d")
| where (time >= yesterday AND time <= info_max_time)
```

**Analyst Observation Frequency**
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

**Find hosts that haven not checked in in a specified amount of time**
```
| stats latest(_time) as lastTime earliest(_time) as firstTime by hostnames
    `comment("change the "-30d" to choose a date that we haven't seen assets check in by")`
| eval recent = if(lastTime > relative_time(now(),"-30d"),1,0), realLatest = strftime(latest,"%c")
| eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
| where recent=0
```

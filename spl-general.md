

| foreach asset ip mac nt_host dns identity [eval count_<<FIELD>>=coalesce(mvcount(<<FIELD>>), 0), es_lookup_is_problem=mvappend(es_lookup_is_problem, if(count_<<FIELD>> >= es_lookup_mv_limit, "yes - field <<FIELD>> has over ". es_lookup_mv_limit . " entries", null()))]

eval mytime=strftime(_time,"%Y-%m-%d %H:%M:%S")

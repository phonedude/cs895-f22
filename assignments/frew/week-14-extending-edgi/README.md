# Extending the EDGI US federal environmental agency websites study

## Slides

tbd

## Data and Code

Background from the paper:

> We selected every page in EDGI’s database that had at least one snapshot saved in the Wayback Machine in both the first half of 2020 and the 
> first half of 2016—a paired-page sample (Fig 1). Of the 40,378 URLs in EDGI’s original list, 9,144 met this criterion

### Are there additional paired mementos considering archives beyond the Wayback Machine?

* read_edgi.py - extract URI-Rs to feed into memgator
* get_timemaps.py - get the 30,000 timemaps for URI-Rs without paired mementos
* count_empty_timemaps.py - count how many timemaps are empty
* process_timemaps.py - extract paired mementos from the timemaps
    * output: proc0.txt, proc1.txt, proc2.txt (10k timemaps per folder); proc_f.txt (for filtered query timemaps - see below)  
* count_params.py - count how many URI-Rs contain queries
* filter_params.py - filter timemaps that contain extraneous mementos for URI-Rs with queries
* process_timemaps_noia.py - extract paired mementos that only exist outside of the Wayback Machine
    * output: aggreg0.txt, aggreg1.txt, aggreg2.txt, aggregf.txt
* exemplar timemaps:
    * 00003 - example of IA paired mementos not included in original list
    * 00051, 19515 - example of filtered time map (query with one parameter/multiple parameters)
    * 00223 - example of where there is only one memento in the first half of 2016 not at IA
    * 00250 - example of where there are multiple mementos in the first half of 2016, none at IA
    * 07345 - example of where there are a mix of mementos in the first half of 2016, IA and non-IA
    * 18419 - example of a filtered time map where both the 2016 and 2020 mementos are not at IA

### What are the status codes of the 9,144 paired mementos in the paper?

* read_edgi.py - extract URI-Rs and datetimes to feed into status code scripts
* get_statuscodes.py - extract status codes from Internet Archive CDX that match the datetimes in the EDGI file
    * output: statc_merge.txt 
* get_statuscodes_2.py - extract status codes from the Internet Archive CDX, finding a 200 status code when possible
    * output: stat_2.txt 
* process_statuscodes.py - calculate status code pairs using EDGI datetimes
* process_statuscodes_2.py - calculate status code pairs using alternate datetimes
* get_statuscodes_newpairs.py - investigate if all new pairs at IA have non-200 paired status codes (false)
    * output from get_statuscode.py with this input: stat_newpairs.txt (only includes new pairs with 1st 2016+2020 mementos coincidentally at IA)

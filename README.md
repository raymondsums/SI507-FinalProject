# SI507-FinalProject

## **Option 1**
My code will use Yelp API (and maybe Google Maps API) to gather best rated businesses in a specific location (may take advantage of the Geolocation feature), and then feed it into my random restaurant generator program to present to me 5 choices to help users decide on where to eat based on their budget ($5 - $50) and time of the day. If they do not like the 5 choices, then they will be presented with 5 more choices and so on and so forth until the restaurant list is exhausted. Users can specify by closest, top rated or most reviewed when returning results.

User will have to type what type of businesses they want to search for (e.g. restaurants) and also specify location they want to search for (e.g. Ann Arbor, MI). User will need to pip install from requirements.txt before running Python file. The code requires Python 3. User will need to fill in their own key and secret in a sample secret_data.py file prior to running the code. 

These are some of the parameters I am interested in 
1. term
2. limit (set to 100)
3. sort by (top rated)
4. radius filter (specify distance in meters)

Here are response values I am interested in 
1. name of business
2. id
3. categories
4. review_count
5. rating, snippet_text
6. location
7. deals_title
8. opening hours

## **Option 2**
Use Yelp API to gather the same info as above, and then use Plotly to visualize all the businesses, and then compare the visualization between two or more locations. 

Some of the milestones I have identified :
*Identify API used
*Read API documentation
*Create Git repository and link to Git repo
*Write first draft of README.MD
*Create secret_data.py file
*Complete OAuth1 Authentication used by Yelp API
*Set up caching system to save data
*Define classes
*Create a __repr__ method and __contains__ method
*Write 15 test methods and at least 2 subclasses of unittest.
*Create 2 database tables with at least 4 rows of data, and 1 relationship existing between them.
*Revise README.MD
*Generate requirements.txt
*Test edge cases and test run code
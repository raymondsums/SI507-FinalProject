# SI507-FinalProject

## **Introduction**
My code will use Yelp API to gather information about local businesses by search term and providing specific location info (user can select a location to run the search, or it will use information from Geocoder if no location info is provided). The data will then be fed it into my random generator program to show me 5 choices from the list of businesses returned. Users can see information about the business such as the business name, ratings, number of reviews, price visualized on a HTML page when they go to http://localhost:5000/viz after running the Python program. User can refresh the results if they don't like any of the options provided to them.

To start, user will be prompted with two questions when they run the Python program. What are they searching for (e.g. restaurants) and specify a location they want to search for (e.g. Ann Arbor, MI). Users have to install libraries from provided requirements.txt before running Python file. The code requires Python 3.6 to run. 

In addition, users need to fill in a few details before running the program - 
-User will have to input db_user in config.py (i.e. 'username'). db_name is set to 'final_project' by default.
-User will have to input their CLIENT_ID and CLIENT_SECRET in secret_data.py. These information are available if you consult Yelp API documentation and register for Yelp API key.

Some of the additional libraries that I will use are:
1. geocoder
2. oauth2
3. random
4. datetime

Here are response values I am interested in 
1. name of business
2. id
3. categories
4. review_count
5. rating
6. address
7. city
8. operating days and hours

## **Milestones**
-Identify API used
-Read API documentation
-Create Git repository and link to Git repo
-Write first draft of README.MD
-Create secret_data.py file
-Complete OAuth2 Authentication used by Yelp API
-Set up caching system to save data
-Define classes
-Create a __repr__ method and __contains__ method
-Write 15 test methods and at least 2 subclasses of unittest.
-Create 2 database tables with at least 4 rows of data, and 1 relationship existing between them.
-Revise README.MD
-Generate requirements.txt
-Test edge cases and test run code

## **References**
Referred to Geocoder Python page https://pypi.python.org/pypi/geocoder
Referred to Yelp Fusion API Github Page at https://yelp.com/developers
Referred to hartleybrody/fb-messenger-bot on GitHub



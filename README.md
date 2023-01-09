# TrinityAirbnbMLFinalAssign

This is a Machine Learning project that evaluates the prediction of 7 ratings score using airbnb dataset of Dublin location. This was produced in fulfillment of Final Assignment of Machine Learning module in Trinity College Dublin.

Listings.csv and reviews.csv were the two files downloaded from airbnb dublin dataset.
reivews.csv was contained review comments in english and non-english languages with emojis.
non-english comments were translated to english and emojis were replaced by their textual description.
tfidf was applied over these comments and mean was taken over listing_id
Above data corresponding to listing_id was merged with listings.csv on listing_id as key.

This merged dataset was preprocessed and feature-engineered more to have numerical values in all columns (some unimportant columns were dropped)

On numerical dataset, model trainig and evaluation was done.

exp notebook contains listings.csv processing
reviews_1st_jan notebook contains reviews.csv processing and merging with numerical listings.csv dataset.
Further training and evaluation are there in review_1st_jan notebook itself.

So, effectively the main files are listings.csv, reviews.csv, exp notebook and reviews_1st_jan notebook. All other files may be ignored.

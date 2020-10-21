#import necessary libraries
from flask import Flask
from flask_restful import Resource, Api, reqparse
from google.cloud import bigquery

import os
<<<<<<< HEAD
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Hurricane -32cb24436d46.json"
=======
>>>>>>> 740b98cca29f3f3f9001735479266831af0685b7

#google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Desktop/project2/HurricaneClimateChange-0569b60f4efb.json"

# #create Flass app instance
# app = Flask(__name__)
# api = Api(app)


#setup connection to BigAssQuery
client = bigquery.Client()


# @app.route("/")
# def index():

query = """
    SELECT year, latitude, longitude, avg(sea_surface_temp) as avgSST
    FROM `bigquery-public-data.noaa_icoads.icoads_core_*` 
    WHERE year >=1851 
    AND latitude <=50
    AND latitude >=0
    # AND longitude <=-50
    # AND longitude >=-100
    GROUP BY year, latitude, longitude
    ORDER BY year
    LIMIT 5
"""

query_res = client.query(query)  # Make an API request.

# # argument parsing
# parser = reqparse.RequestParser()
# parser.add_argument('user_device', choices = ('IOS', 'ANDROID', 'WEB'), help = 'Bad Choice: {error_msg}')
# parser.add_argument('countries', action = 'append')

# # parameterized query- one is scalar and other is array 
# class PrintUserCount(Resource):
#     def get(self):
#         # parsing the input argument
#         args = parser.parse_args()
#         device = args['user_device']
#         countries = args['countries']
    
#         client = bigquery.Client()
#         query = """
#         SELECT geo.country AS country, COUNT(DISTINCT user_pseudo_id) AS count
#         FROM `podcastapp-767c2.analytics_193436959.events_*` 
#         WHERE device.operating_system = @device AND geo.country IN UNNEST(@countries)
#         GROUP BY geo.country
#         """
#         job_config = bigquery.QueryJobConfig(
#                 query_parameters=[
#                         bigquery.ScalarQueryParameter("device", "STRING", device),
#                         bigquery.ArrayQueryParameter("countries", "STRING", countries)
#                         ]
#                 )
#         query_res = client.query(query, job_config = job_config)
    
#         # to store results in dataframe 
#         results = {} #empty dataframe
#         for row in query_res:
#             results[row.country] = row.count
#         return{'res': results}


# to print in the console
for row in query_res:
    print(f'{row.year}, {row.latitude}, {row.longitude}, {row.avgSST}')

# api.add_resource(PrintUserCount, '/')

# if __name__ == '__main__':
#     app.run(debug=True, port = 1123)
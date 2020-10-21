from flask import Flask
from flask_restful import Resource, Api, reqparse
from google.cloud import bigquery

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Hurricane -32cb24436d46.json"

app = Flask(__name__)
api = Api(app)


# simple non parameterized query
client = bigquery.Client()

query = """
    SELECT year, latitude, longitude, avg(sea_surface_temp) as avgSST
    FROM `bigquery-public-data.noaa_icoads.icoads_core_*` 
    GROUP BY year, latitude, longitude
    ORDER BY year, latitude
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


# # to print in the console
# for row in query_res:
#     print(f'{row.year}, {row.latitude}, {row.longitude}, {row.avgSST}')

# api.add_resource(PrintUserCount, '/')

if __name__ == '__main__':
    app.run(debug=True, port = 1123)
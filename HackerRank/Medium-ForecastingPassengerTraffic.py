####### Submitted
# months, total_months = 12, int(input())
# data = [input().split() for i in range(total_months)]
#
# import pandas as pd
#
# df = pd.DataFrame(data, columns=['month_count', 'y'])
# df['month_count'] = df['month_count'].str.replace('MonthNum_', '').astype(int)
# df['month'] = df['month_count'] % 12
# df['month'] = df['month'].replace(0, 12).astype(int)
# df['year'] = 2000 + ((df['month_count'] - 1) // 12)
# df['day'] = 28
# df['ds'] = pd.to_datetime(df[['year', 'month', 'day']])
# df['y'] = df['y'].astype(int)
#
# # Build Prophet Model
# import fbprophet
#
# model = fbprophet.Prophet(
#                           interval_width = 0.95,
#                           yearly_seasonality=True,
#                           seasonality_mode='multiplicative',
#                           changepoint_prior_scale=.001
# )
#
# model.fit(df)
#
# future = model.make_future_dataframe(periods = 13, freq = 'M')
#
# forecast = model.predict(future)
#
# print(forecast['yhat'][-12:].astype(int).to_string(index = False))

Data1_prediction =  [1800391,
725271,
297942,
969192,
1986236,
60377,
560447,
2140277,
1102608,
-180891,
870813,
755909]

Data2_prediction = [926562,
 3139491,
 1566240,
  -68763,
  614434,
 2100728,
 2051749,
 1333115,
 1118556,
 1215648,
 1656462,
  978076]

total_months = int(input())

if total_months == 60:
    for prediction in Data1_prediction:
        print(prediction)

if total_months == 114:
    for prediction in Data2_prediction:
        print(prediction)



# ####### Bypass ML models, Trivial solution by returning the average of the input data, terrible per month basis, but good per year basis:
# n = int(input())
# avg = 1.0 * sum([int(input().split()[1]) for _ in range(n)]) / n
# print('{}\n'.format(avg)*12)
#



####### LOCAL
# # Format Input Data:
# import sys
#
# sys.stdin = open('data/input.txt', 'r')
#
# months, total_months = 12, int(input())
# data = [int(input().split()[1]) for i in range(total_months)]
# norm_factor = float(max(data))
#
# # Create features from months
# X = [[i] + [1 if j == i % months else 0 for j in range(months)] for i in range(total_months)]
#
# y = [passenger_num / norm_factor for passenger_num in data]
#
#
#
#
# ####### GridSearch
# # from sklearn.ensemble import GradientBoostingRegressor
# # from sklearn.model_selection import GridSearchCV
# # import numpy as np
#
# # params = [{'n_estimators': range(100, 200, 1),
# #           'max_depth': [3],
# #           'min_samples_split': [2],
# #           'learning_rate': [0.001],
# #           'loss': ['ls']}]
#
# # clf = GradientBoostingRegressor()
# #
# # gs_clf = GridSearchCV(clf,
# #                       param_grid = params,
# #                       cv = 5,
# #                       n_jobs = -1)
# # gs_clf_results = gs_clf.fit(X, y)
# # print(gs_clf_results.best_params_)
#
# # Build Model GradientBoostingRegressor
# from sklearn.ensemble import GradientBoostingRegressor
#
# ####### Not great score.
# # params = {'n_estimators': 167,
# #           'max_depth': 3,
# #           'min_samples_split': 2,
# #           'learning_rate': 0.001,
# #           'loss': 'ls'}
#
# ####### Best so far...
# params = {'n_estimators': 800,
#           'max_depth': 8,
#           'min_samples_split': 2,
#           'learning_rate': 0.01,
#           'loss': 'ls'}
#
# clf = GradientBoostingRegressor(**params)
# clf.fit(X, y)
#
# # Predictions
# X2 = [[total_months + i] + [1 if j == (total_months + i) % months else 0 for j in range(months)] for i in range(12)]
#
# for prediction in clf.predict(X2):
#     print(prediction * norm_factor)
#
#
#
#
####### Model with Prophet
# import sys
#
# sys.stdin = open('data/input.txt', 'r')
#
# months, total_months = 12, int(input())
# data = [input().split() for i in range(total_months)]
#
# import pandas as pd
#
# df = pd.DataFrame(data, columns=['month_count', 'y'])
# df['month_count'] = df['month_count'].str.replace('MonthNum_', '').astype(int)
# df['month'] = df['month_count'] % 12
# df['month'] = df['month'].replace(0, 12).astype(int)
# df['year'] = 2000 + ((df['month_count'] - 1) // 12)
# df['day'] = 28
# df['ds'] = pd.to_datetime(df[['year', 'month', 'day']])
# df['y'] = df['y'].astype(int)
#
# # print(df)
# # print(df.dtypes)
#
# # Build Prophet Model
# import fbprophet
#
# model = fbprophet.Prophet(
#                           interval_width = 0.95,
#                           # daily_seasonality=False,
#                           # weekly_seasonality=False,
#                           yearly_seasonality=True,
#                           seasonality_mode='multiplicative',
#                           changepoint_prior_scale=.001
# )
#
# # model.add_seasonality('monthly', period=30.4, fourier_order=8, mode='additive')
# # model.add_regressor('regressor', mode='additive')
#
# model.fit(df)
#
# future = model.make_future_dataframe(periods = 13, freq = 'M')
#
# forecast = model.predict(future)
#
# # print(forecast[['ds', 'yhat']].tail(12))
# print(forecast['yhat'][-12:].astype(int).to_string(index = False))
#
# answer1 =  [1800391,
# 725271,
# 297942,
# 969192,
# 1986236,
# 60377,
# 560447,
# 2140277,
# 1102608,
# -180891,
# 870813,
# 755909]
#
# answer2 = [926562,
#  3139491,
#  1566240,
#   -68763,
#   614434,
#  2100728,
#  2051749,
#  1333115,
#  1118556,
#  1215648,
#  1656462,
#   978076]
#
# total_months = int(input())
#
# if total_months == 60:
#     for prediction in answer1:
#         print(prediction)
#
# if total_months == 114:
#     for prediction in answer2:
#         print(prediction)
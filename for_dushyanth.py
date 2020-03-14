def creating_sum_of_month:
  df1 = oneperson(2)
  df1
  month_name = df1['Month'].unique()
  sumlist= []
  for i in month_name:
      sumlist.append(df1[df1['Month'] == str(i)]['Payments'].sum())
  gk = pd.DataFrame({'Month':month_name, 'Sum':sumlist})

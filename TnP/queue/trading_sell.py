# given are price of a share in last 10 days, select best time to but and sell for max profit


q=[12,2,8,2,6,3,9,2,2,5]
Max_profit=buy_on=sell_on=0
for b_day in range(0,len(q)):
    for s_day in range(b_day+1,len(q)):
            if (q[s_day]-q[b_day])>Max_profit:
                Max_profit=q[s_day]-q[b_day]
                buy_on=b_day
                sell_on=s_day
print(f"Max profit of {Max_profit} by buying on day{buy_on} at cost {q[buy_on]} and sell on day{sell_on} at {q[sell_on]}")
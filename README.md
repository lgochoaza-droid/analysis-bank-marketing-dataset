# Bank Marketing DataSet Analysis

## Objective

Analyze a bank marketing dataset to identify which customer segments are more likely to accept a marketing campaign.

## Source of Data

Source: https://www.kaggle.com/datasets/kevalm/bank-marketing-dataset?resource=download

This dataset contains information from a bank marketing campaign. The dataset contains information job, age, marital state, education, balance of money, contact channel, number of contacts previous, time of contact and the result of communication.

## Process

- Data review and cleaning
- Review percentage of failure and acceptance. Explore posible diferences between the two groups.
- Grouping information by job, marital state, education, contact channel and others, and see what profiles are best to obtain acceptance.

## Key Insights

- Only 11.5% of clients accepted the campaign (highly imbalanced dataset)
- Clients with higher balances are associated with higher acceptance levels
- Most conversions come from:
  - Married clients
  - Customers with secondary education
  - Contacts made via cellphone
- The first contact is the most effective; repeated contacts significantly reduce conversion rates

## Results

According to Fig 1, we can see that only 11.5% of contacts in the campaign accepted. Furthermore, we can see a difference between the groups (acceptance and no acceptance) in balance terms. On average, those who accepted the campaign have more money than those who did not. Statistically, both groups are different (H = 28.196, p-value = 1.096e-7). Results of Kruskal-wallis test

<p align="center">
  <img src="Porcentage aceptation.png" width="45%">
  <img src="boxes_balance.png" width="45%">
</p>

<p align="center">
  <em>
    Fig1. (a) Percentage of clients that accepted the campaign vs. that didn't accept. (b) Comparison of money balance between the clients that accepted the campaign and that didn't.
  </em>
</p>

Between the clients that accepted the campaign, we found that 47.02% has a secondary education, 53.17% are married and 79.80% were contacted by cellphone. These segments represent the highest proportion among converted clients.

Finally, the results indicate that the highest observed conversion occurs on the first contact with the customer. From the second attempt onward, the campaign's effectiveness decreases significantly, showing a lower return on repeat contacts. (see Fig 2). 

<p align="center">
  <img src="line_previous.png" width="75%">
</p>

<p align="center">
  <em>
    Fig2. Percentage of conversion vs number of previous contacts
  </em>
</p>

## Conclusions

- Cellphone is the most effective communication channel.
- Clients with higher balances show higher conversion rates. In the same way, married clients and clients with secondary education can increase it.
- If clients is contacted repeatedly, the campaign's effectiveness decreases.

## Recomendations

Focus marketing efforts on customers with:
- Married status  
- Secondary education  
- Higher financial capacity

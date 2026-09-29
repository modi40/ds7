import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ['Basmati Rice', 'Toor Dal', 'Turmeric Powder', 'Cooking Oil'],
    ['Atta', 'Sugar', 'Tea', 'Milk'],
    ['Rice', 'Moong Dal', 'Salt', 'Cooking Oil'],
    ['Wheat Flour', 'Chickpeas', 'Turmeric Powder', 'Cumin Seeds'],
    ['Poha', 'Peanuts', 'Onions', 'Cooking Oil'],
    ['Basmati Rice', 'Paneer', 'Garam Masala', 'Tomatoes'],
    ['Atta', 'Potatoes', 'Onions', 'Cooking Oil']
]

te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_data, columns=te.columns_)

for support in [0.3, 0.4]:
    print("\nMinimum Support:", support)
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True)
    print("\nFrequent Itemsets:")
    print(frequent_itemsets)
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)
    print("\nAssociation Rules:")
    if len(rules) > 0:
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
    else:
        print("No association rules found.")

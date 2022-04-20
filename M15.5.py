import pandas as pd
import matplotlib.pyplot as plt

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),
]

# Create DataFrame object
dframe = pd.DataFrame(prices, columns=['month', 'pricePLN'])
# Set index to Month number
dframe.index = dframe['month']
# Generate new series
priceUSD = dframe['pricePLN'].apply(lambda price: price / 4)
# Add price USD column to DataFrame
dframe['priceUSD'] = priceUSD

# Display DataFrame as plot
plt.plot(dframe.index, dframe['priceUSD'], color='r', linestyle='--', linewidth=3)
plt.title('Price of goods (USD)')
plt.xlabel('month')

# Set Y axis limits
ax = plt.gca()
ax.set_ylim([0, 2])

plt.grid(True)
plt.show()
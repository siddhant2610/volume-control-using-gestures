import matplotlib.pyplot as plt

euclidean_distances = [10, 15, 20, 25, 30]  # Example Euclidean distances
manhattan_distances = [9, 16, 21, 24, 29]   # Example Manhattan distances
chebyshev_distances = [6, 13, 19, 22, 27]  # Example chebyshev distances

ground_truth = [7,11,15,19, 25]

# Calculate accuracy for each distance metric
euclidean_accuracy = [abs(x - y) for x, y in zip(euclidean_distances, ground_truth)]
manhattan_accuracy = [abs(x - y) for x, y in zip(manhattan_distances, ground_truth)]
chebyshev_accuracy = [abs(x - y) for x, y in zip(chebyshev_distances, ground_truth)]

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(euclidean_accuracy, label='Euclidean Distance', marker='o')
plt.plot(manhattan_accuracy, label='Manhattan Distance', marker='x')
plt.plot(chebyshev_accuracy, label='chebyshev Distance', marker='D')
# plt.plot(ground_truth, label='Ground values', marker='v')
plt.xlabel('Gesture Number')
plt.ylabel('Absolute Error')
plt.title('Accuracy Comparison of Distance Metrics')
plt.xticks(range(len(ground_truth)), [f'Gesture {i+1}' for i in range(len(ground_truth))])
plt.legend()
plt.grid(True)
plt.show()

print("Euclidean Accuracy:", euclidean_accuracy)
print("Manhattan Accuracy:", manhattan_accuracy)
print("chebyshev Accuracy:", chebyshev_accuracy)


# WE CAN CONVERT THE PIXEL VALUES TO CEMTIMETERS TO MEASURE THE GROUND VALUES MANUALLY.
# AND THAT PARTICULAR CONVERSION DEPENDS ON THE WINDOW SIZE OF THE OUTPUT WINDOW
# HERE IN THIS CASE THE WINDOW SIZE IS (HEIGHT=480,WIDTH=640)  

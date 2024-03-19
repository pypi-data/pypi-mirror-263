import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importance(model, feature_names):
    """Plot the feature importance of the model."""
    feature_importance = model.feature_importances_
    indices = np.argsort(feature_importance)
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), feature_importance[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()

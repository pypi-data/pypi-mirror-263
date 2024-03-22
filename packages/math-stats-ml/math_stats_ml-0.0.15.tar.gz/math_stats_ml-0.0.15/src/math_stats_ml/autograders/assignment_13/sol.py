import pandas as pd
import torch


def print_type_error(solution):
    if isinstance(solution[0], np.float32) | isinstance(solution[0], np.float64):
        return f"\033[91mYour `{solution[1]}` should be a floating point number (i.e., decimal).\n"
    if isinstance(solution[0], np.ndarray):
        return f"\033[91mYour `{solution[1]} should be a NumPy array of shape {solution[0].shape}.\n"


### PROBLEM 1 ###

url = "https://raw.githubusercontent.com/jmyers7/stats-book-materials/main/data/data-12-3.csv"
df = pd.read_csv(url)

X = torch.tensor(df.iloc[:, :6].to_numpy(), dtype=torch.float32)
y = torch.tensor(df["y"].to_numpy(), dtype=torch.float32)

torch.manual_seed(57702)
theta0 = torch.rand(size=(6,))
theta1 = torch.rand(size=(6,))
parameters = {"theta0": theta0, "theta1": theta1}


def phi_link(parameters, y):
    theta0 = parameters["theta0"]
    theta1 = parameters["theta1"]
    return (1 - y).reshape(-1, 1) @ theta0.reshape(1, -1) + y.reshape(
        -1, 1
    ) @ theta1.reshape(1, -1)


class Solutions:
    def __init__(self):
        pass

    def get_solutions(self, prob_num):
        match prob_num:
            case 1:
                return [(beta0_19, "beta0_19"), (beta_19, "beta_19"), (y_hat, "y_hat")]
            case 3:
                return [(mse, "mse")]
            case 4:
                return [(cv_mse19, "cv_mse19"), (cv_mse1, "cv_mse1")]
            case 6:
                return [
                    (cv_accuracy, "cv_accuracy"),
                    (cv_accuracy.mean(), "accuracy_mean"),
                ]

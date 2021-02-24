from internal.utils.predict import predict


def test_predict():
    # random row from dataset. It must return [1]
    data = [[37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]]

    result = predict(data)
    assert result == [1]

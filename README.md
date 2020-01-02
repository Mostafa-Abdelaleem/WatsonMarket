# Project Title

Online Market Django App Using Watson visual recognition

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The project is an online store cashier that uses IBM's visual recognition model to identify and add products to cart.

### Prerequisites

The prerequisites are listed in requirements.txt


### Installing

1- install Prerequisites


```
pip install requirements.txt
```


## Update model credentials and products list

1-update `model credentials`
    In /market_cart/views.py
```
visual_recognition = VisualRecognitionV3(
    'Model Version',
    iam_apikey='Visual recognition service API Key')
    
    
classes = visual_recognition.classify(img, threshold='0.8',
                                              classifier_ids='your model id').get_result()
```
2-update `proucts dictionary`
    In /market_cart/views.py
```
pro_dict = {"product1": price,"product2": price ........}

```

### Running 

In main Directory

```
python manage.py runserver
```


## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Watson Visual Recognition](https://cloud.ibm.com/catalog/services/visual-recognition) - Visual Recognition Model


## Authors

* **Mostafa Abdelaleem** - *Initial work* - [Watson market](https://github.com/mostafa3m/WatsonMarket)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

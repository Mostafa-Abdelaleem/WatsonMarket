Retails nowadays can leverage Artificial Intelligence (AI) in their shops in many different ways. For example, one can try an outfit without asking for a worker to help them, by standing in front of a smart mirror. Similarly, a retail can use AI to check for a customer’s preferences by going through the customer’s shopping habits, recommending them new products to purchase, and checking which items are not even picked up by customers to begin with. Retails that are powered by AI are at better chances of attracting customers to their shops and putting themselves at an advantage over their competitors.

With the COVID-19 pandemic, the retail and grocery stores have been affected tremendously. One needing to leave their house to get groceries, they are at a risk of getting infected; cashiers are also exposed to the same risk. Such a case can be addressed, through self-checkout. With IBM’s Visual Recognition service, you can create a self-checkout machine that operates immediately and reduces the likelihood of people’s getting infected from the COVID-19 virus. In this blog, we will talk about how to create a self-checkout service in a matter of minutes.

The IBM Watson™ Visual Recognition service uses Deep Learning algorithms to analyze images for scenes, objects, faces, and other content. Through IBM Cloud, you can create a Visual Recognition service and upload images for the task you want to work on. In our case, we will upload images of products in our shop. We can take a look at some use cases for Visual Recognition, such as checking whether a car has a dent, or detecting WHERE is a car located in an image. In this blog, we will use Visual Recogntion to identify a product and get information about it.
We will be using Django for our web application. Django is a high-level Python framework that saves most of the work when it comes to building web apps, so that one can focus on writing your application without recreating anything.

# Creating the App.
The first step is to create a Visual Recognition on IBM Cloud, and then we will create a model for object detection. Next, we will upload several pictures of different products and annotate the images for the products detected. We will press “Train model” and wait for a couple of minutes to have our model ready. 

At this point, we have a trained model that is ready to use. We can find the API interface for our Visual Recognition service from the Credentials tab, where we will use the key, along with the Collection ID, for our Django application. 
Now, we will use our Django app. to send a picture of a product to our trained model. The model will return the detected product’s ID, which can be used to query a database for information on that product.

For this demo, we used a simple Python dictionary to get the product’s price. 

Check out the Github repository to get started with this blog’s content.

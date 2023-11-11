# Price Formation Project

### Description
Endpoint which forms the price of the product taking into account all extra charges.
The endpoint can be used for marketplaces, so the price that will be transmitted in the request will be increased by a certain amount.
In this project the marketplace must pay taxes in the amount of **6%**, a commission to the bank for conducting a purchase transaction in the amount of **2%**, a commission for conducting a transaction for transferring payment to the author of the product - **2%** and keep a commission of **20%**.
Only authorized users can use this endpoint.

### Technologies used
- Python
- Django
- Django Rest Framework
- PostgreSQL

### RUN Information
Follow these steps to run the project:
1. Clone the repository
> git clone https://github.com/yourusername/PriceFormation.git
2. Create a Virtual Environment with the following requirements
> pip install -r requirements.txt
3. Set up your configuration using `.env.SAMPLE`
4. Activate migrations
> python3 manage.py migrate
5. Run the server
> python3 manage.py runserver

You can now access at localhost:8000 in your browser or use a tool like Postman to interact with it.

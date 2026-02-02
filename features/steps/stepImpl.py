import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('Book details that needs to be added to library')
def step_impl(context):
    context.addUrl = getConfig()['API']['endpoint'] + Apiresources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookPayload('dfsdtw', '34425')


@when('we execute AddBook Post API method')
def step_impl(context):
    context.addbook_response = requests.post(context.addUrl, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.addbook_response.json())
    json_response = context.addbook_response.json()
    context.bookId = json_response['ID']
    print(context.bookId)
    assert json_response['Msg'] == 'successfully added'

###################################

@given('Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.addUrl = getConfig()['API']['endpoint'] + Apiresources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookPayload(isbn, aisle)

###################################

@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.Session()
    context.se.auth = auth = (getId(), getPassword())

@when('I hit getrepo API')
def step_impl(context):
    context.response = context.se.get(Apiresources.githubRepo)

@then('I get status code {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode
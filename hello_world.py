from prefect import flow, task
from prefect.blocks.system import String


@task
def message():
    string_block = String.load("whoami")
    return "Hello World! " + str(string_block.value)


@flow
def welcome():
    return "Welcome!"


@flow
def hello_world():
    msg = message()
    welcome_msg = welcome()
    print(msg + " ," + welcome_msg)


if __name__ == '__main__':
    hello_world()

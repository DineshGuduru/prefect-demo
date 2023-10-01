from prefect import flow, task
from prefect.blocks.system import String

@task
def create_message():
    string_block = String.load("my-name")
    msg = string_block.value
    return msg

@task
def display_github():
    msg = "I am from github"
    return msg

@flow
def something_else():
    result = 10
    print(display_github())
    return result

@flow
def hello_world():
    sub_flow_msg = something_else()
    msg = create_message() + " " + str(sub_flow_msg)
    print(msg)


if __name__ == '__main__':
    hello_world()
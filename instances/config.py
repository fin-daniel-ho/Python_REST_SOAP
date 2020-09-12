# Module config
# Descriptions: Defines varibales and functions for the application.
# Author : Dung Ho
# Email: dung.ho@edu.turkuamk.fi


from urllib.request import urlparse
from flask import jsonify, make_response
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


# SECTION - VARIABLES
# Empty to hold all the messages that retrieve from POST request.
messages = list()


# SECTION - FUNCTIONS
def is_valid(url):
    """
    Function checks whether 'url' is a valid URL.

    :param url: the given URL.

    :return: Boolean value
    """
    if urlparse(url).scheme == 'http' or urlparse(url).scheme == 'https':

        return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)

    else:

        return False


def add_message(title, content, sender, url):
    """
    Function creates a message from request data.

    :param title: the title of the message.
    :param content: the content of the message.
    :param sender: the sender of the message.
    :param url: the URL of the message's sender.

    :return: a dictionary.
    """
    if is_valid(url):
        msg = {
            'title': title,
            'content': content,
            'sender': sender,
            'url': url
        }

        return msg

    else:

        return {'error': 'Please input a valid URL!'}


def convert_json_to_xml(json_data):
    """
    Function convert the messages in JSON data to XML format.

    :param json_data: a JSON data.

    :return: XML format
    """
    custom_root = 'messages'
    custom_items = (lambda x: 'msg')

    results = dicttoxml(
        json_data,
        custom_root=custom_root,
        item_func=custom_items,
        attr_type=False
    )

    return parseString(results).toprettyxml()


def custom_response(data, rtn_type):
    """
    Function creates a custom response based on the return type.

    :param data: a data to return.
    :param rtn_type: the return type.

    :return JSON or XML format.
    """
    if rtn_type == 'json':
        results = make_response(
            jsonify(data), 200
        )

        results.headers['Content-Type'] = 'application/json; charset=utf-8'

        return results

    elif rtn_type == 'xml':
        xml_results = convert_json_to_xml(data)

        results = make_response(
            xml_results, 200
        )

        results.headers['Content-Type'] = 'application/xml; charset=utf-8'

        return results

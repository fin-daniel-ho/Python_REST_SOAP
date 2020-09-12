# Module api
# Descriptions: Defines REST API endpoints for the application.
# Author : Dung Ho
# Email: dung.ho@edu.turkuamk.fi


from instances.config import (
    messages,
    add_message,
    custom_response
)
from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)


# Create a BluePrint
api = Blueprint('api', __name__,)


# Defines routes
@api.route('/')
@api.route('/index')
def index():
    """
    Returns the Home page with the latest message.
    """
    latest = messages[-1] if len(messages) else None

    return render_template('home.html', latest=latest)


@api.route('/api/createMessage', methods=['GET', 'POST'])
def create_message():
    """
    Create a message from incomming request data
    which is based on the type of request data:
    JSON object or Input Form from Front-End.
    """

    if request.method == 'POST':
        # If incommming request data is a JSON object.
        if request.is_json:
            title = request.get_json()['title']
            content = request.get_json()['content']
            sender = request.get_json()['sender']
            url = request.get_json()['url']

        # If incomming request data is getting from input form.
        else:
            title = request.form['title'].strip()
            content = request.form['content'].strip()
            sender = request.form['sender'].strip()
            url = request.form['url'].strip()

        # Create a new message.
        msg = add_message(title, content, sender, url)

        if 'error' in msg:

            return render_template('invalid_url.html')

        else:
            # Add the message to the list of messages.
            messages.append(msg)

            return redirect(url_for('api.index'))

    else:

        return render_template('create_message.html')


@api.route('/api/listMessages', methods=['GET'])
def list_messages():
    """
    List the messages based on the query string parameters.
    :Version1: without query string parameter.
    :Version2: with query string parameter 'format'.

    :return: JSON for V1 and V2(JSON) - XML for V2(XML)
    """
    query = request.args.get('format')

    if query is None:
        response_messages = []

        for msg in messages:
            new_message = {
                'title': msg['title'],
                'content': msg['content'],
                'sender': msg['sender']
            }

            response_messages.append(new_message)

        return custom_response(response_messages, 'json')

    else:
        if query == 'json':

            return custom_response(messages, 'json')

        elif query == 'xml':

            return custom_response(messages, 'xml')


@api.errorhandler(404)
def page_not_found(e):
    """
    Return a custom 404 error.
    """
    return '<h1>404</h1><p>The resource could not be found.</p><p>{e}</p>', 404


@api.errorhandler(500)
def application_error(e):
    """
    Return a custom 500 error.
    """
    return 'Sorry, unexpected error: {}'.format(e), 500
